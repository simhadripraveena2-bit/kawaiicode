import { useState, useEffect } from "react";
import { useParams, Link, useLocation } from "wouter";
import { useLesson, useCompleteLesson } from "@/hooks/use-lessons";
import { Button } from "@/components/ui/button";
import { Quiz } from "@/components/Quiz";
import { ArrowLeft, CheckCircle2 } from "lucide-react";
import ReactMarkdown from "react-markdown";
import { motion } from "framer-motion";
import { ScrollArea } from "@/components/ui/scroll-area";
import confetti from "canvas-confetti";

export default function LessonView() {
  const { slug } = useParams();
  const [location, setLocation] = useLocation();
  const { data: lesson, isLoading } = useLesson(slug || "");
  const { mutate: completeLesson } = useCompleteLesson();
  
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);
  const [lessonCompleted, setLessonCompleted] = useState(false);

  useEffect(() => {
    // Reset state when slug changes
    setCurrentQuizIndex(0);
    setLessonCompleted(false);
  }, [slug]);

  if (isLoading) {
    return (
      <div className="flex h-[calc(100vh-64px)] items-center justify-center">
        <div className="animate-spin text-4xl">🌸</div>
      </div>
    );
  }

  if (!lesson) {
    return (
      <div className="flex flex-col items-center justify-center h-[calc(100vh-64px)] gap-4">
        <h2 className="font-display text-2xl font-bold">Lesson not found!</h2>
        <Link href="/">
          <Button>Return Home</Button>
        </Link>
      </div>
    );
  }

  const handleQuizComplete = () => {
    if (currentQuizIndex < (lesson.quizzes?.length || 0) - 1) {
      setCurrentQuizIndex(prev => prev + 1);
    } else {
      setLessonCompleted(true);
      completeLesson(lesson.id);
      confetti({
        particleCount: 200,
        spread: 100,
        origin: { y: 0.6 }
      });
    }
  };

  return (
    <div className="h-[calc(100vh-64px)] flex flex-col md:flex-row overflow-hidden bg-background">
      {/* Sidebar / Content Area */}
      <motion.div 
        initial={{ x: -50, opacity: 0 }}
        animate={{ x: 0, opacity: 1 }}
        className="w-full md:w-1/2 flex flex-col border-r border-border/50 bg-white/50 backdrop-blur-sm"
      >
        <div className="p-4 border-b border-border/50 flex items-center gap-4 bg-white/50">
          <Link href="/">
            <Button variant="ghost" size="icon" className="rounded-xl">
              <ArrowLeft className="w-5 h-5" />
            </Button>
          </Link>
          <div>
            <div className="text-xs font-bold text-muted-foreground uppercase tracking-wider">Level {lesson.order}</div>
            <h1 className="font-display text-xl font-bold line-clamp-1">{lesson.title}</h1>
          </div>
        </div>

        <ScrollArea className="flex-1 p-6 md:p-8">
          <div className="markdown-content max-w-2xl mx-auto pb-20">
            <ReactMarkdown>{lesson.content}</ReactMarkdown>
          </div>
        </ScrollArea>
      </motion.div>

      {/* Interactive Area */}
      <motion.div 
        initial={{ x: 50, opacity: 0 }}
        animate={{ x: 0, opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="w-full md:w-1/2 bg-secondary/10 flex flex-col p-6 md:p-8 overflow-y-auto"
      >
        <div className="flex-1 flex flex-col justify-center max-w-xl mx-auto w-full">
          {!lessonCompleted ? (
            lesson.quizzes && lesson.quizzes.length > 0 ? (
              <>
                <div className="mb-6 flex items-center justify-between text-sm font-bold text-muted-foreground">
                  <span>Quiz Progress</span>
                  <span>{currentQuizIndex + 1} / {lesson.quizzes.length}</span>
                </div>
                {/* Progress Bar */}
                <div className="w-full h-2 bg-muted rounded-full mb-8 overflow-hidden">
                  <motion.div 
                    className="h-full bg-primary"
                    initial={{ width: 0 }}
                    animate={{ width: `${((currentQuizIndex) / lesson.quizzes.length) * 100}%` }}
                  />
                </div>
                
                <Quiz 
                  key={currentQuizIndex} // Force remount on change
                  quiz={lesson.quizzes[currentQuizIndex]} 
                  onComplete={handleQuizComplete} 
                />
              </>
            ) : (
              <div className="text-center p-8 bg-card rounded-3xl border-2 border-dashed border-border">
                <p className="text-lg font-medium text-muted-foreground mb-4">
                  No quizzes for this lesson yet. Just mark it as done!
                </p>
                <Button size="lg" onClick={() => {
                   setLessonCompleted(true);
                   completeLesson(lesson.id);
                }}>
                  Complete Lesson
                </Button>
              </div>
            )
          ) : (
            <motion.div 
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              className="bg-card rounded-3xl p-8 border-2 border-primary/20 shadow-xl text-center"
            >
              <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                <CheckCircle2 className="w-10 h-10 text-green-600" />
              </div>
              <h2 className="font-display text-3xl font-bold mb-2">Lesson Complete!</h2>
              <p className="text-muted-foreground font-medium mb-8">
                You've mastered this topic and earned {lesson.xp} XP.
              </p>
              
              <div className="space-y-3">
                <Button className="w-full h-12 text-lg" onClick={() => setLocation("/")}>
                  Back to Map
                </Button>
                {/* Could add 'Next Lesson' logic here if we knew the next slug */}
              </div>
            </motion.div>
          )}
        </div>
      </motion.div>
    </div>
  );
}
