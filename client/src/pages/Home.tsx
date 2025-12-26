import { useLessons, useUserProgress } from "@/hooks/use-lessons";
import { LessonCard } from "@/components/LessonCard";
import { Skeleton } from "@/components/ui/skeleton";
import { motion } from "framer-motion";
import { ScrollArea } from "@/components/ui/scroll-area";

export default function Home() {
  const { data: lessons, isLoading: isLoadingLessons } = useLessons();
  const { data: progress, isLoading: isLoadingProgress } = useUserProgress();

  if (isLoadingLessons || isLoadingProgress) {
    return (
      <div className="container mx-auto px-4 py-12 max-w-5xl">
        <div className="mb-12 text-center space-y-4">
          <Skeleton className="h-12 w-64 mx-auto rounded-xl" />
          <Skeleton className="h-6 w-96 mx-auto rounded-lg" />
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <Skeleton key={i} className="h-64 rounded-3xl" />
          ))}
        </div>
      </div>
    );
  }

  // Determine locked status based on progress
  // First lesson is always unlocked. Subsequent lessons unlock if previous is completed.
  const processedLessons = lessons?.map((lesson, index) => {
    const isCompleted = progress?.some(p => p.lessonId === lesson.id && p.completed) || false;
    
    // First lesson unlocked by default.
    // Others unlocked if previous index was completed.
    const isLocked = index === 0 ? false : !(progress?.some(p => p.lessonId === lessons[index - 1].id && p.completed));

    return { ...lesson, isCompleted, isLocked };
  });

  return (
    <div className="container mx-auto px-4 py-12 max-w-5xl min-h-screen">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-16"
      >
        <span className="inline-block py-1 px-3 rounded-full bg-primary/10 text-primary font-bold text-sm mb-4">
          World 1: Python Basics
        </span>
        <h1 className="font-display text-4xl md:text-5xl font-bold mb-4 text-foreground">
          Level Select
        </h1>
        <p className="text-xl text-muted-foreground max-w-xl mx-auto font-medium">
          Choose a level to start your journey. Complete challenges to unlock new stages!
        </p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 relative z-10">
         {/* Drawing a connector line behind cards could be cool, but tricky responsively.
             For now, let's stick to a grid that looks good. */}
        {processedLessons?.map((lesson, index) => (
          <LessonCard
            key={lesson.id}
            index={index}
            lesson={lesson}
            isCompleted={lesson.isCompleted}
            isLocked={lesson.isLocked}
          />
        ))}
      </div>
    </div>
  );
}
