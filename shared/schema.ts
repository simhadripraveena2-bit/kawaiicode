import { pgTable, text, serial, integer, boolean, timestamp, jsonb } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";
import { users } from "./models/auth";
import { relations } from "drizzle-orm";

export * from "./models/auth";

export const lessons = pgTable("lessons", {
  id: serial("id").primaryKey(),
  slug: text("slug").notNull().unique(),
  title: text("title").notNull(),
  description: text("description").notNull(),
  content: text("content").notNull(), // Markdown content
  order: integer("order").notNull(), // To sort lessons
  xp: integer("xp").notNull().default(10),
});

export const quizzes = pgTable("quizzes", {
  id: serial("id").primaryKey(),
  lessonId: integer("lesson_id").references(() => lessons.id).notNull(),
  question: text("question").notNull(),
  options: jsonb("options").$type<string[]>().notNull(),
  correctAnswer: integer("correct_answer").notNull(), // Index of correct option
});

export const progress = pgTable("user_progress", {
  id: serial("id").primaryKey(),
  userId: text("user_id").notNull(), // References auth.users.id (varchar)
  lessonId: integer("lesson_id").references(() => lessons.id).notNull(),
  completed: boolean("completed").default(false),
  completedAt: timestamp("completed_at"),
});

// Relations
export const lessonsRelations = relations(lessons, ({ many }) => ({
  quizzes: many(quizzes),
}));

export const quizzesRelations = relations(quizzes, ({ one }) => ({
  lesson: one(lessons, {
    fields: [quizzes.lessonId],
    references: [lessons.id],
  }),
}));

export const progressRelations = relations(progress, ({ one }) => ({
  lesson: one(lessons, {
    fields: [progress.lessonId],
    references: [lessons.id],
  }),
}));

// Schemas
export const insertLessonSchema = createInsertSchema(lessons).omit({ id: true });
export const insertQuizSchema = createInsertSchema(quizzes).omit({ id: true });
export const insertProgressSchema = createInsertSchema(progress).omit({ id: true, completedAt: true });

// Types
export type Lesson = typeof lessons.$inferSelect;
export type Quiz = typeof quizzes.$inferSelect;
export type UserProgress = typeof progress.$inferSelect;
