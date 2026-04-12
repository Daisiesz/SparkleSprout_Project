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
        self.root.geometry("920x720")
        self.root.configure(bg="#a5f3fc")
        self.root.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):
        header = tk.Frame(self.root, bg="#ff6bcb", height=110)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🌟 SparkleSprout", 
                 font=("Comic Sans MS", 38, "bold"), 
                 bg="#ff6bcb", fg="white").pack(pady=15)

        tk.Label(header, text="SuperKids Learning Hub • Ages 4–12", 
                 font=("Arial", 16), bg="#ff6bcb", fg="white").pack()

        tk.Label(self.root, text="What adventure shall we go on today? 🌈", 
                 font=("Comic Sans MS", 22, "bold"), bg="#a5f3fc", fg="#1e2937").pack(pady=50)

        btn_frame = tk.Frame(self.root, bg="#a5f3fc")
        btn_frame.pack(pady=20)

        # Questly Button
        tk.Button(btn_frame, text="🚀 Questly\nKids Adventure Planner", 
                  font=("Arial", 18, "bold"), bg="#10b981", fg="white",
                  width=28, height=5, command=self.launch_questly).grid(row=0, column=0, padx=40, pady=25)

        # Calculator Button
        tk.Button(btn_frame, text="🧮 Kids Calculator", 
                  font=("Arial", 18, "bold"), bg="#3b82f6", fg="white",
                  width=28, height=5, command=self.launch_calculator).grid(row=0, column=1, padx=40, pady=25)

        footer = tk.Label(self.root, 
                          text="Built with love for curious kids in Kenya 🇰🇪 | SparkleSprout_Project",
                          font=("Arial", 11), bg="#a5f3fc", fg="#475569")
        footer.pack(side="bottom", pady=50)

    def launch_questly(self):
        try:
            subprocess.Popen([sys.executable, "questly.py"])
            messagebox.showinfo("Questly", "Opening Questly - Kids Adventure Planner 🌟")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Questly:\n{str(e)}")

    def launch_calculator(self):
        try:
            subprocess.Popen([sys.executable, "-m", "kids_calculator.gui"])
            messagebox.showinfo("Kids Calculator", "Opening Kids Calculator 🧮")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Calculator:\n{str(e)}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    if not os.path.exists("questly.py"):
        messagebox.showerror("Missing File", "questly.py is missing!\nPlease add it to the project folder.")
        sys.exit(1)
    
    app = SparkleSproutHub()
    app.run()