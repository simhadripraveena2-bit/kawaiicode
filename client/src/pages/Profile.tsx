import { useAuth } from "@/hooks/use-auth";
import { useUserProgress, useLessons } from "@/hooks/use-lessons";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { User, Trophy, Flame, Calendar, LogOut } from "lucide-react";
import { motion } from "framer-motion";

export default function Profile() {
  const { user, logout } = useAuth();
  const { data: progress } = useUserProgress();
  const { data: lessons } = useLessons();

  if (!user) return null;

  const completedCount = progress?.filter(p => p.completed).length || 0;
  const totalXp = progress?.reduce((acc, p) => {
    // Find lesson to get XP value
    const lesson = lessons?.find(l => l.id === p.lessonId);
    return acc + (p.completed ? (lesson?.xp || 0) : 0);
  }, 0) || 0;

  return (
    <div className="container mx-auto px-4 py-12 max-w-4xl">
      <div className="grid md:grid-cols-3 gap-8">
        
        {/* User Card */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="col-span-1"
        >
          <div className="bg-card rounded-3xl p-8 border border-border/50 shadow-lg text-center relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-24 bg-gradient-to-br from-primary/20 to-secondary/20 z-0" />
            
            <div className="relative z-10">
              <div className="w-24 h-24 mx-auto bg-white rounded-full p-1 shadow-lg mb-4">
                <img 
                  src={user.profileImageUrl || `https://api.dicebear.com/7.x/avataaars/svg?seed=${user.username}`}
                  alt={user.username}
                  className="w-full h-full rounded-full object-cover"
                />
              </div>
              
              <h2 className="font-display text-2xl font-bold mb-1">{user.username}</h2>
              <p className="text-muted-foreground font-medium mb-6 text-sm">{user.email}</p>
              
              <div className="flex justify-center gap-2 mb-8">
                <span className="bg-primary/10 text-primary px-3 py-1 rounded-full text-xs font-bold uppercase">
                  Student
                </span>
                <span className="bg-accent/10 text-accent px-3 py-1 rounded-full text-xs font-bold uppercase">
                  Lvl 1
                </span>
              </div>

              <Button variant="outline" className="w-full border-2" onClick={() => logout()}>
                <LogOut className="w-4 h-4 mr-2" />
                Sign Out
              </Button>
            </div>
          </div>
        </motion.div>

        {/* Stats Grid */}
        <div className="col-span-1 md:col-span-2 space-y-6">
          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 }}
          >
            <h3 className="font-display text-xl font-bold mb-4">Statistics</h3>
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-card p-6 rounded-3xl border border-border/50 shadow-sm flex items-center gap-4">
                <div className="bg-yellow-100 p-3 rounded-2xl text-yellow-600">
                  <Trophy className="w-8 h-8" />
                </div>
                <div>
                  <div className="text-3xl font-display font-bold text-foreground">{totalXp}</div>
                  <div className="text-sm font-medium text-muted-foreground">Total XP</div>
                </div>
              </div>

              <div className="bg-card p-6 rounded-3xl border border-border/50 shadow-sm flex items-center gap-4">
                <div className="bg-orange-100 p-3 rounded-2xl text-orange-600">
                  <Flame className="w-8 h-8" />
                </div>
                <div>
                  <div className="text-3xl font-display font-bold text-foreground">{completedCount}</div>
                  <div className="text-sm font-medium text-muted-foreground">Lessons Done</div>
                </div>
              </div>
            </div>
          </motion.div>

          <motion.div
             initial={{ opacity: 0, y: 20 }}
             animate={{ opacity: 1, y: 0 }}
             transition={{ delay: 0.2 }}
          >
            <h3 className="font-display text-xl font-bold mb-4">Achievements</h3>
            <div className="bg-card p-6 rounded-3xl border border-border/50 shadow-sm">
              <div className="text-center py-8 text-muted-foreground">
                <div className="bg-muted w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Trophy className="w-8 h-8 text-muted-foreground/50" />
                </div>
                <p className="font-medium">Complete more lessons to unlock achievements!</p>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
}
