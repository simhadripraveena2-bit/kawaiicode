import { Link } from "wouter";
import { Button } from "@/components/ui/button";
import { AlertTriangle } from "lucide-react";

export default function NotFound() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-background p-4 text-center">
      <div className="bg-primary/10 p-6 rounded-full mb-6 animate-bounce">
        <AlertTriangle className="h-16 w-16 text-primary" />
      </div>
      
      <h1 className="font-display text-5xl font-bold mb-4 text-foreground">404</h1>
      <p className="text-xl text-muted-foreground mb-8 max-w-md font-medium">
        Oops! Looks like this page got lost in the void. Let's get you back on track.
      </p>

      <Link href="/">
        <Button size="lg" className="h-14 px-8 text-lg">
          Back to Home
        </Button>
      </Link>
    </div>
  );
}
