import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { api } from "@shared/routes";
import { setupAuth, registerAuthRoutes } from "./replit_integrations/auth";
import { isAuthenticated } from "./replit_integrations/auth";
import { db } from "./db";
import { lessons, quizzes } from "@shared/schema";

export async function registerRoutes(
  httpServer: Server,
  app: Express
): Promise<Server> {
  // Auth Setup
  await setupAuth(app);
  registerAuthRoutes(app);

  // API Routes
  app.get(api.lessons.list.path, async (req, res) => {
    const lessons = await storage.getAllLessons();
    res.json(lessons);
  });

  app.get(api.lessons.get.path, async (req, res) => {
    const lesson = await storage.getLessonBySlug(req.params.slug);
    if (!lesson) {
      return res.status(404).json({ message: "Lesson not found" });
    }
    res.json(lesson);
  });

  app.post(api.lessons.complete.path, isAuthenticated, async (req, res) => {
    const lessonId = parseInt(req.params.id);
    const userId = (req.user as any).claims.sub;
    
    const lesson = await storage.getLessonById(lessonId);
    if (!lesson) {
      return res.status(404).json({ message: "Lesson not found" });
    }

    await storage.markLessonComplete(userId, lessonId);
    res.json({ success: true, xpAwarded: lesson.xp });
  });

  app.get(api.user.progress.path, isAuthenticated, async (req, res) => {
    const userId = (req.user as any).claims.sub;
    const progress = await storage.getUserProgress(userId);
    res.json(progress);
  });

  // Initial seeding
  await seedDatabase();

  return httpServer;
}

// Seeding function
export async function seedDatabase() {
  const existing = await storage.getAllLessons();
  if (existing.length === 0) {
    const lessonsData = [
      {
        slug: "hello-python",
        title: "Introduction to Python",
        description: "Your first step into the world of Python programming! ✨",
        content: `
# Hello World! 👋

Welcome to **KawaiiCode**! Python is a super fun and powerful language. 
Let's start by saying hello to the world.

\`\`\`python
print("Hello, World!")
\`\`\`

The \`print()\` function shows text on the screen. It's that easy!
        `.trim(),
        order: 1,
        xp: 10
      },
      {
        slug: "variables",
        title: "Magic Variables",
        description: "Learn how to store data like a pro wizard! 🧙‍♀️",
        content: `
# Variables 📦

Variables are like little boxes where you can store information.

\`\`\`python
name = "Sakura"
power_level = 9000
\`\`\`

You can use them later in your code!
        `.trim(),
        order: 2,
        xp: 20
      }
    ];

    const insertedLessons = await db.insert(lessons).values(lessonsData).returning();

    // Add quizzes
    if (insertedLessons.length > 0) {
      await db.insert(quizzes).values([
        {
          lessonId: insertedLessons[0].id,
          question: "What function do we use to output text?",
          options: ["echo()", "console.log()", "print()", "write()"],
          correctAnswer: 2
        },
        {
          lessonId: insertedLessons[1].id,
          question: "How do you assign a value to a variable?",
          options: ["name : 'Sakura'", "name = 'Sakura'", "var name = 'Sakura'", "set name 'Sakura'"],
          correctAnswer: 1
        }
      ]);
    }
  }
}
