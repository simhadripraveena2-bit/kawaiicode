import { db } from "./db";
import { lessons, quizzes, progress, type Lesson, type Quiz, type UserProgress } from "@shared/schema";
import { eq, and } from "drizzle-orm";
import { authStorage } from "./replit_integrations/auth/storage";

export interface IStorage {
  // Lessons
  getAllLessons(): Promise<Lesson[]>;
  getLessonBySlug(slug: string): Promise<(Lesson & { quizzes: Quiz[] }) | undefined>;
  getLessonById(id: number): Promise<Lesson | undefined>;
  
  // Progress
  getUserProgress(userId: string): Promise<UserProgress[]>;
  markLessonComplete(userId: string, lessonId: number): Promise<void>;
  
  // Auth (re-export or delegate)
  getUser(id: string): Promise<any>;
}

export class DatabaseStorage implements IStorage {
  async getAllLessons(): Promise<Lesson[]> {
    return await db.select().from(lessons).orderBy(lessons.order);
  }

  async getLessonBySlug(slug: string): Promise<(Lesson & { quizzes: Quiz[] }) | undefined> {
    const lesson = await db.query.lessons.findFirst({
      where: eq(lessons.slug, slug),
      with: {
        quizzes: true,
      }
    });
    return lesson;
  }

  async getLessonById(id: number): Promise<Lesson | undefined> {
    const [lesson] = await db.select().from(lessons).where(eq(lessons.id, id));
    return lesson;
  }

  async getUserProgress(userId: string): Promise<UserProgress[]> {
    return await db.select().from(progress).where(eq(progress.userId, userId));
  }

  async markLessonComplete(userId: string, lessonId: number): Promise<void> {
    const existing = await db.select().from(progress).where(
      and(eq(progress.userId, userId), eq(progress.lessonId, lessonId))
    );

    if (existing.length === 0) {
      await db.insert(progress).values({
        userId,
        lessonId,
        completed: true,
        completedAt: new Date(),
      });
    }
  }

  async getUser(id: string) {
    return authStorage.getUser(id);
  }
}

export const storage = new DatabaseStorage();
