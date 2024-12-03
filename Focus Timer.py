import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkCheckBox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import time


class FlipClockApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Focus Clock By Kingshuk Mondal(KM23MS005)")
        self.root.configure(bg="#1c1c1c")
        self.running = False

        # Fonts and Flip Clock Properties
        self.font = ImageFont.truetype("arial.ttf", 60)
        self.flip_animation_duration = 500  # milliseconds for flip effect
        self.is_pinned = tk.BooleanVar(value=False)  # Variable for "Pin this window"

        # Full Layout Frame
        self.main_frame = tk.Frame(self.root, bg="#1c1c1c")
        self.main_frame.pack(fill="both", expand=True)

        # Input Section
        input_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Time (HH:MM:SS):", fg="white", bg="#1c1c1c", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
        self.time_input = CTkEntry(input_frame, width=120, font=("Helvetica", 12))
        self.time_input.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Your Goal:", fg="white", bg="#1c1c1c", font=("Helvetica", 12)).grid(row=1, column=0, padx=5)
        self.highlight_input = CTkEntry(input_frame, width=200, font=("Helvetica", 12))
        self.highlight_input.grid(row=1, column=1, padx=5)

        CTkButton(input_frame, text="Start Timer", command=self.start_timer).grid(row=2, column=0, columnspan=2, pady=10)

        # Highlighted Text Section
        self.highlight_label = CTkLabel(self.main_frame, text="", font=("Neon Tubes", 20), text_color="#00FF00", fg_color="black", corner_radius=10)
        self.highlight_label.pack(pady=10)

        # Flip Clock Display
        self.canvas = tk.Canvas(self.main_frame, width=350, height=300, bg="#1c1c1c", highlightthickness=0)
        self.canvas.pack()

        # Pin Window Checkbox
        self.pin_checkbox = CTkCheckBox(self.main_frame, text="Pin this window", variable=self.is_pinned, command=self.toggle_pin, fg_color="#00FF00")
        self.pin_checkbox.pack(pady=10)

        # Minimized View Button
        self.minimized_frame = None

    def draw_flip_animation(self, time_text):
        """Draw flip-style animation for the clock."""
        img = Image.new("RGB", (300, 150), color="#1c1c1c")
        draw = ImageDraw.Draw(img)
        draw.text((75, 25), time_text, font=self.font, fill="white")
        photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(150, 75, image=photo)
        self.canvas.image = photo

    def start_timer(self):
        if self.running:
            messagebox.showinfo("Timer Active", "Timer is already running!")
            return

        timer_str = self.time_input.get()
        highlight_text = self.highlight_input.get()
        self.highlight_label.configure(text=highlight_text)

        try:
            h, m, s = map(int, timer_str.split(":"))
            total_seconds = h * 3600 + m * 60 + s
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter time in HH:MM:SS format.")
            return

        self.running = True
        self.countdown(total_seconds)
        self.minimize_interface()

    def countdown(self, seconds):
        if seconds < 0:
            self.draw_flip_animation("00:00:00")
            self.running = False
            messagebox.showinfo("Time's Up!", "Focus session complete!")
            return

        h, m, s = seconds // 3600, (seconds % 3600) // 60, seconds % 60
        time_text = f"{h:02}:{m:02}:{s:02}"
        self.draw_flip_animation(time_text)
        self.root.after(1000, self.countdown, seconds - 1)

    def minimize_interface(self):
        """Minimize the interface to a small settings box."""
        self.main_frame.pack_forget()

        if not self.minimized_frame:
            self.minimized_frame = tk.Frame(self.root, bg="#1c1c1c")
            self.minimized_frame.pack(fill="both", expand=True)

            tk.Label(self.minimized_frame, text="⏲️ Timer Running", fg="white", bg="#1c1c1c", font=("Helvetica", 16)).pack(pady=10)
            CTkButton(self.minimized_frame, text="Open Settings", command=self.restore_interface).pack(pady=10)

    def restore_interface(self):
        """Restore the full interface from the minimized settings box."""
        self.minimized_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def toggle_pin(self):
        """Toggle the 'always on top' property of the window."""
        self.root.attributes("-topmost", self.is_pinned.get())


# Main Application
if __name__ == "__main__":
    root = CTk()
    app = FlipClockApp(root)
    root.mainloop()
