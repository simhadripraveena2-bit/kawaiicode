import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { api, buildUrl } from "@shared/routes";
import { useToast } from "@/hooks/use-toast";

export function useLessons() {
  return useQuery({
    queryKey: [api.lessons.list.path],
    queryFn: async () => {
      const res = await fetch(api.lessons.list.path);
      if (!res.ok) throw new Error("Failed to fetch lessons");
      return api.lessons.list.responses[200].parse(await res.json());
    },
  });
}

export function useLesson(slug: string) {
  return useQuery({
    queryKey: [api.lessons.get.path, slug],
    queryFn: async () => {
      const url = buildUrl(api.lessons.get.path, { slug });
      const res = await fetch(url);
      if (res.status === 404) return null;
      if (!res.ok) throw new Error("Failed to fetch lesson");
      return api.lessons.get.responses[200].parse(await res.json());
    },
    enabled: !!slug,
  });
}

export function useUserProgress() {
  return useQuery({
    queryKey: [api.user.progress.path],
    queryFn: async () => {
      const res = await fetch(api.user.progress.path, { credentials: "include" });
      if (!res.ok) throw new Error("Failed to fetch progress");
      return api.user.progress.responses[200].parse(await res.json());
    },
  });
}

export function useCompleteLesson() {
  const queryClient = useQueryClient();
  const { toast } = useToast();

  return useMutation({
    mutationFn: async (lessonId: number) => {
      const url = buildUrl(api.lessons.complete.path, { id: lessonId });
      const res = await fetch(url, {
        method: api.lessons.complete.method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({}),
        credentials: "include",
      });

      if (!res.ok) throw new Error("Failed to complete lesson");
      return api.lessons.complete.responses[200].parse(await res.json());
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: [api.user.progress.path] });
      toast({
        title: "Level Up! 🎉",
        description: `You earned ${data.xpAwarded} XP!`,
        className: "bg-primary text-primary-foreground border-none shadow-lg",
      });
    },
    onError: () => {
      toast({
        title: "Error",
        description: "Failed to save progress. Try again!",
        variant: "destructive",
      });
    },
  });
}
