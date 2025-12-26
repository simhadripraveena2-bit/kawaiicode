import { z } from 'zod';
import { insertLessonSchema, insertProgressSchema, lessons, quizzes, progress } from './schema';

export const errorSchemas = {
  validation: z.object({
    message: z.string(),
    field: z.string().optional(),
  }),
  notFound: z.object({
    message: z.string(),
  }),
  internal: z.object({
    message: z.string(),
  }),
};

export const api = {
  lessons: {
    list: {
      method: 'GET' as const,
      path: '/api/lessons',
      responses: {
        200: z.array(z.custom<typeof lessons.$inferSelect>()),
      },
    },
    get: {
      method: 'GET' as const,
      path: '/api/lessons/:slug',
      responses: {
        200: z.custom<typeof lessons.$inferSelect & { quizzes: typeof quizzes.$inferSelect[] }>(),
        404: errorSchemas.notFound,
      },
    },
    complete: {
      method: 'POST' as const,
      path: '/api/lessons/:id/complete',
      input: z.object({}),
      responses: {
        200: z.object({ success: z.boolean(), xpAwarded: z.number() }),
        404: errorSchemas.notFound,
      },
    }
  },
  user: {
    progress: {
      method: 'GET' as const,
      path: '/api/user/progress',
      responses: {
        200: z.array(z.custom<typeof progress.$inferSelect>()),
      },
    },
  },
};

export function buildUrl(path: string, params?: Record<string, string | number>): string {
  let url = path;
  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (url.includes(`:${key}`)) {
        url = url.replace(`:${key}`, String(value));
      }
    });
  }
  return url;
}
