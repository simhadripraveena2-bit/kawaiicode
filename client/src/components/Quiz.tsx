import { useState } from "react";
import { type Quiz as QuizType } from "@shared/schema";
import { Button } from "@/components/ui/button";
import { motion, AnimatePresence } from "framer-motion";
import { Check, X, ArrowRight, HelpCircle, CheckCircle2 } from "lucide-react";
import confetti from "canvas-confetti";
import { cn } from "@/lib/utils";

interface QuizProps {
  quiz: QuizType;
  onComplete: () => void;
}

export function Quiz({ quiz, onComplete }: QuizProps) {
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  const handleSubmit = () => {
    if (selectedOption === null) return;
    
    const correct = selectedOption === quiz.correctAnswer;
    setIsCorrect(correct);
    setHasSubmitted(true);

    if (correct) {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#FFB7B2', '#E0BBE4', '#957DAD']
      });
    }
  };

  const handleNext = () => {
    onComplete();
    // Reset state for next time this component might be used
    setSelectedOption(null);
    setHasSubmitted(false);
    setIsCorrect(false);
  };

  return (
    <div className="bg-card rounded-3xl p-6 border-2 border-border/50 shadow-sm">
      <div className="flex items-center gap-3 mb-6">
        <div className="bg-primary/10 p-2 rounded-xl text-primary">
          <HelpCircle className="w-6 h-6" />
        </div>
        <h3 className="font-display text-xl font-bold">Pop Quiz!</h3>
      </div>

      <p className="text-lg font-medium mb-6 leading-relaxed">
        {quiz.question}
      </p>

      <div className="space-y-3 mb-6">
        {quiz.options.map((option, index) => {
          const isSelected = selectedOption === index;
          const showSuccess = hasSubmitted && index === quiz.correctAnswer;
          const showError = hasSubmitted && isSelected && index !== quiz.correctAnswer;

          return (
            <motion.button
              key={index}
              whileHover={!hasSubmitted ? { scale: 1.01 } : {}}
              whileTap={!hasSubmitted ? { scale: 0.99 } : {}}
              onClick={() => !hasSubmitted && setSelectedOption(index)}
              className={cn(
                "w-full p-4 rounded-xl text-left font-medium transition-all border-2 flex items-center justify-between group",
                !hasSubmitted && isSelected && "border-primary bg-primary/5 ring-2 ring-primary/20",
                !hasSubmitted && !isSelected && "border-border hover:border-primary/50 hover:bg-muted/30",
                showSuccess && "border-green-500 bg-green-50 text-green-700",
                showError && "border-red-500 bg-red-50 text-red-700",
                hasSubmitted && !showSuccess && !showError && "opacity-50 grayscale"
              )}
            >
              <span>{option}</span>
              {showSuccess && <Check className="w-5 h-5 text-green-600" />}
              {showError && <X className="w-5 h-5 text-red-600" />}
            </motion.button>
          );
        })}
      </div>

      <AnimatePresence mode="wait">
        {!hasSubmitted ? (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <Button 
              className="w-full" 
              size="lg" 
              onClick={handleSubmit}
              disabled={selectedOption === null}
            >
              Check Answer
            </Button>
          </motion.div>
        ) : (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="flex flex-col gap-4"
          >
            <div className={cn(
              "p-4 rounded-xl text-sm font-bold flex items-center gap-2",
              isCorrect ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"
            )}>
              {isCorrect ? (
                <>
                  <CheckCircle2 className="w-5 h-5" />
                  Correct! Great job!
                </>
              ) : (
                <>
                  <X className="w-5 h-5" />
                  Not quite right. Try again!
                </>
              )}
            </div>
            
            {isCorrect ? (
               <Button className="w-full" size="lg" onClick={handleNext}>
                 Continue <ArrowRight className="ml-2 w-4 h-4" />
               </Button>
            ) : (
              <Button 
                variant="secondary" 
                className="w-full" 
                onClick={() => {
                  setHasSubmitted(false);
                  setSelectedOption(null);
                }}
              >
                Try Again
              </Button>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
