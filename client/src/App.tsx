import { Switch, Route, useLocation } from "wouter";
import { queryClient } from "./lib/queryClient";
import { QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";
import { useAuth } from "@/hooks/use-auth";
import { NavBar } from "@/components/NavBar";
import { Loader2 } from "lucide-react";

import Home from "@/pages/Home";
import Landing from "@/pages/Landing";
import LessonView from "@/pages/LessonView";
import Profile from "@/pages/Profile";
import NotFound from "@/pages/not-found";

function Router() {
  const { user, isLoading } = useAuth();
  
  if (isLoading) {
    return (
      <div className="flex h-screen w-full items-center justify-center bg-background">
        <Loader2 className="h-12 w-12 animate-spin text-primary" />
      </div>
    );
  }

  // If user is NOT logged in, show Landing page for root.
  // Otherwise show Home (Level Select).
  // Protected routes will redirect or show empty if not auth'd.

  return (
    <Switch>
      <Route path="/">
        {user ? <Home /> : <Landing />}
      </Route>
      
      <Route path="/lesson/:slug">
        {user ? <LessonView /> : <Landing />}
      </Route>

      <Route path="/profile">
        {user ? <Profile /> : <Landing />}
      </Route>

      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <div className="min-h-screen bg-background font-sans text-foreground selection:bg-primary/30">
          <NavBar />
          <Router />
        </div>
        <Toaster />
      </TooltipProvider>
    </QueryClientProvider>
  );
}

export default App;
