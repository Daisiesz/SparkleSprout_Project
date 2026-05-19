# main_hub.py
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class SparkleSproutHub:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌟 SparkleSprout Hub - Fun Learning for Kids!")
        self.root.geometry("1000x720")
        self.root.configure(bg="#a5f3fc")
        self.root.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#ff6bcb", height=120)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🌟 SparkleSprout", 
                 font=("Comic Sans MS", 40, "bold"), 
                 bg="#ff6bcb", fg="white").pack(pady=20)

        tk.Label(header, text="SuperKids Learning Hub • Ages 4–12", 
                 font=("Arial", 16), bg="#ff6bcb", fg="white").pack()

        # Welcome
        tk.Label(self.root, text="What would you like to do today, superstar? 🌈", 
                 font=("Comic Sans MS", 22, "bold"), bg="#a5f3fc").pack(pady=40)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#a5f3fc")
        btn_frame.pack(pady=20)

        # Questly
        tk.Button(btn_frame, text="🚀 Questly\nAdventure Planner", 
                  font=("Arial", 16, "bold"), bg="#10b981", fg="white",
                  width=26, height=5, command=self.launch_questly).grid(row=0, column=0, padx=25, pady=20)

        # Calculator
        tk.Button(btn_frame, text="🧮 Kids Calculator", 
                  font=("Arial", 16, "bold"), bg="#3b82f6", fg="white",
                  width=26, height=5, command=self.launch_calculator).grid(row=0, column=1, padx=25, pady=20)

        # SparkleQuiz - New Button
        tk.Button(btn_frame, text="🌟 SparkleQuiz\nLearn & Test Yourself", 
                  font=("Arial", 16, "bold"), bg="#8b5cf6", fg="white",
                  width=26, height=5, command=self.launch_quiz).grid(row=0, column=2, padx=25, pady=20)

        # Footer
        tk.Label(self.root, text="Built with ❤️ for curious kids in Kenya 🇰🇪 | SparkleSprout_Project", 
                 font=("Arial", 11), bg="#a5f3fc", fg="#475569").pack(side="bottom", pady=50)

    def launch_questly(self):
        try:
            import subprocess
            import os
            import time

            questly_path = os.path.abspath("questly.py")

            if not os.path.exists(questly_path):
                messagebox.showerror("File Missing", "questly.py was not found in the project folder!")
                return

            # Strongest method for Windows
            if os.name == 'nt':  # Windows
                subprocess.Popen(
                    [sys.executable, questly_path],
                    creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.DETACHED_PROCESS,
                    shell=False
                )
            else:
                subprocess.Popen([sys.executable, questly_path])

            # Small delay so the message doesn't appear too fast
            time.sleep(0.8)
            messagebox.showinfo("Questly Launched ✅", 
                "Questly should be opening now.\n\nIf it still doesn't appear, try closing the hub and running questly.py directly.")

        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch Questly:\n\n{str(e)}")
    
    def launch_calculator(self):
        try:
            subprocess.Popen([sys.executable, "-m", "kids_calculator.gui"])
            messagebox.showinfo("Launching Calculator", "Kids Calculator is opening! 🧮")
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch Calculator:\n{str(e)}")
    
    def launch_quiz(self):
        try:
            # Better import handling
            import sys
            if "sparkle_quiz" not in sys.path:
                sys.path.insert(0, ".")
            
            from sparkle_quiz.quiz_gui import SparkleQuiz
            quiz = SparkleQuiz()
            quiz.run()
        except Exception as e:
            messagebox.showerror("SparkleQuiz Error", 
                f"Failed to launch Quiz:\n{str(e)}\n\nMake sure sparkle_quiz folder exists with all files.")
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    if not os.path.exists("questly.py"):
        messagebox.showwarning("Missing File", "questly.py not found. Some features may be missing.")
    
    app = SparkleSproutHub()
    app.run()