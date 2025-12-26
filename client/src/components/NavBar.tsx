import { Link, useLocation } from "wouter";
import { useAuth } from "@/hooks/use-auth";
import { Button } from "@/components/ui/button";
import { LogOut, User, Trophy, Sparkles } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export function NavBar() {
  const { user, logout } = useAuth();
  const [location] = useLocation();

  return (
    <nav className="sticky top-0 z-50 w-full bg-background/80 backdrop-blur-lg border-b border-border/50">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 group cursor-pointer">
          <div className="bg-primary p-2 rounded-xl group-hover:rotate-12 transition-transform">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <span className="font-display font-bold text-xl tracking-tight text-foreground group-hover:text-primary transition-colors">
            Kawaii<span className="text-primary">Code</span>
          </span>
        </Link>

        <div className="flex items-center gap-4">
          {user ? (
            <>
              <div className="hidden md:flex items-center gap-2 px-4 py-1.5 bg-secondary/50 rounded-full border border-secondary">
                <Trophy className="w-4 h-4 text-primary" />
                <span className="text-sm font-bold text-secondary-foreground">Lvl 1</span>
              </div>
              
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" size="icon" className="rounded-full overflow-hidden border-2 border-primary/20 hover:border-primary/50">
                    <img 
                      src={user.profileImageUrl || `https://api.dicebear.com/7.x/avataaars/svg?seed=${user.username}`}
                      alt={user.username}
                      className="w-full h-full object-cover"
                    />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end" className="w-56 rounded-2xl p-2">
                  <DropdownMenuLabel className="font-display">My Account</DropdownMenuLabel>
                  <DropdownMenuSeparator />
                  <Link href="/profile">
                    <DropdownMenuItem className="cursor-pointer rounded-xl font-medium focus:bg-primary/10 focus:text-primary">
                      <User className="mr-2 h-4 w-4" />
                      <span>Profile</span>
                    </DropdownMenuItem>
                  </Link>
                  <DropdownMenuItem 
                    className="cursor-pointer rounded-xl font-medium text-destructive focus:bg-destructive/10 focus:text-destructive"
                    onClick={() => logout()}
                  >
                    <LogOut className="mr-2 h-4 w-4" />
                    <span>Log out</span>
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </>
          ) : (
            location !== "/login" && (
              <Button onClick={() => window.location.href = "/api/login"} variant="default" size="sm">
                Start Learning
              </Button>
            )
          )}
        </div>
      </div>
    </nav>
  );
}
