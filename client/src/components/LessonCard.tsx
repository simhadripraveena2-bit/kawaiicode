import { Link } from "wouter";
import { type Lesson } from "@shared/schema";
import { CheckCircle2, Lock, PlayCircle, Star } from "lucide-react";
import { cn } from "@/lib/utils";
import { motion } from "framer-motion";

interface LessonCardProps {
  lesson: Lesson;
  isLocked: boolean;
  isCompleted: boolean;
  index: number;
}

export function LessonCard({ lesson, isLocked, isCompleted, index }: LessonCardProps) {
  const CardContent = (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.1 }}
      className={cn(
        "relative group flex flex-col p-6 rounded-3xl transition-all duration-300 border-2",
        isLocked 
          ? "bg-muted/50 border-transparent cursor-not-allowed grayscale-[0.5]" 
          : "bg-card border-border/50 hover:border-primary/50 hover:shadow-xl hover:shadow-primary/10 hover:-translate-y-1 cursor-pointer"
      )}
    >
      <div className="absolute top-4 right-4">
        {isCompleted ? (
          <div className="bg-green-100 text-green-600 p-2 rounded-full">
            <CheckCircle2 className="w-5 h-5" />
          </div>
        ) : isLocked ? (
          <div className="bg-muted text-muted-foreground p-2 rounded-full">
            <Lock className="w-5 h-5" />
          </div>
        ) : (
          <div className="bg-primary/10 text-primary p-2 rounded-full group-hover:bg-primary group-hover:text-white transition-colors">
            <PlayCircle className="w-5 h-5" />
          </div>
        )}
      </div>

      <div className="mb-4">
        <span className={cn(
          "inline-block px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider",
          isLocked ? "bg-muted text-muted-foreground" : "bg-accent/10 text-accent"
        )}>
          Level {lesson.order}
        </span>
      </div>

      <h3 className="font-display text-xl font-bold mb-2 group-hover:text-primary transition-colors line-clamp-1">
        {lesson.title}
      </h3>
      
      <p className="text-muted-foreground text-sm line-clamp-2 mb-4 font-medium">
        {lesson.description}
      </p>

      <div className="mt-auto flex items-center gap-2 text-xs font-bold text-muted-foreground">
        <Star className="w-4 h-4 text-yellow-400 fill-yellow-400" />
        <span>{lesson.xp} XP</span>
      </div>
    </motion.div>
  );

  if (isLocked) {
    return CardContent;
  }

  return (
    <Link href={`/lesson/${lesson.slug}`} className="block">
      {CardContent}
    </Link>
  );
}
