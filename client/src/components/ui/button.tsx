import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-2xl text-sm font-bold ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 active:scale-95",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow-[0_4px_0_0_rgb(219,39,119)] hover:shadow-[0_2px_0_0_rgb(219,39,119)] hover:translate-y-[2px] active:shadow-none active:translate-y-[4px]",
        secondary: "bg-secondary text-secondary-foreground shadow-[0_4px_0_0_rgb(147,51,234,0.2)] hover:shadow-[0_2px_0_0_rgb(147,51,234,0.2)] hover:translate-y-[2px] active:shadow-none active:translate-y-[4px]",
        outline: "border-2 border-input bg-background hover:bg-accent hover:text-accent-foreground hover:border-accent",
        ghost: "hover:bg-accent/10 hover:text-accent",
        link: "text-primary underline-offset-4 hover:underline",
        game: "bg-gradient-to-b from-blue-400 to-blue-500 text-white border-b-4 border-blue-700 hover:brightness-110 active:border-b-0 active:translate-y-1",
      },
      size: {
        default: "h-11 px-6 py-2",
        sm: "h-9 rounded-xl px-4 text-xs",
        lg: "h-14 rounded-2xl px-10 text-lg",
        icon: "h-11 w-11",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
