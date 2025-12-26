import { useAuth } from "@/hooks/use-auth";
import { Link } from "wouter";
import { Button } from "@/components/ui/button";
import { Sparkles, Code2, Rocket, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

export default function Landing() {
  const { user } = useAuth();

  // If user is logged in, this page won't be shown (redirected in App.tsx)
  // But just in case, or for presentation:
  
  return (
    <div className="min-h-[calc(100vh-64px)] flex flex-col items-center justify-center p-4 relative overflow-hidden">
      {/* Decorative Background Elements */}
      <div className="absolute top-20 left-10 w-32 h-32 bg-primary/10 rounded-full blur-3xl animate-pulse" />
      <div className="absolute bottom-20 right-10 w-48 h-48 bg-accent/10 rounded-full blur-3xl animate-pulse delay-700" />
      
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-center max-w-3xl z-10"
      >
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/50 backdrop-blur-sm border border-white/20 shadow-sm mb-8">
          <Sparkles className="w-4 h-4 text-primary" />
          <span className="text-sm font-bold text-foreground/80">Learn Python the Kawaii Way</span>
        </div>
        
        <h1 className="text-6xl md:text-8xl font-display font-bold mb-6 text-foreground tracking-tight">
          Code with <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-purple-500">Magic</span>
        </h1>
        
        <p className="text-xl md:text-2xl text-muted-foreground mb-12 leading-relaxed max-w-2xl mx-auto font-medium">
          Embark on an epic quest to master Python. Solve puzzles, defeat bugs, and level up your coding skills!
        </p>
        
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Button size="lg" className="h-16 px-10 text-xl shadow-xl shadow-primary/20 hover:shadow-2xl hover:shadow-primary/30" onClick={() => window.location.href = "/api/login"}>
            Start Your Adventure <Rocket className="ml-2 w-6 h-6" />
          </Button>
          <Button size="lg" variant="outline" className="h-16 px-10 text-xl bg-white/50 border-2">
            View Syllabus <Code2 className="ml-2 w-6 h-6" />
          </Button>
        </div>
      </motion.div>

      {/* Hero Image / Mascots */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.3, duration: 0.6 }}
        className="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-5xl px-4"
      >
        {[
          { title: "Interactive Lessons", desc: "Learn by doing with instant feedback", icon: "✨" },
          { title: "Gamified Progress", desc: "Earn XP and unlock achievements", icon: "🏆" },
          { title: "Cute Companions", desc: "Your anime friends cheer you on", icon: "😺" }
        ].map((feature, i) => (
          <div key={i} className="bg-white/40 backdrop-blur-md p-8 rounded-3xl border border-white/50 text-center hover:bg-white/60 transition-colors">
            <div className="text-4xl mb-4">{feature.icon}</div>
            <h3 className="font-display font-bold text-xl mb-2">{feature.title}</h3>
            <p className="text-muted-foreground font-medium">{feature.desc}</p>
          </div>
        ))}
      </motion.div>
    </div>
  );
}
