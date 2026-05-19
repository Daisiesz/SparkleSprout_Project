import tkinter as tk
from tkinter import messagebox
from .quiz_data import get_topics, get_questions
from .quiz_core import QuizTracker

class SparkleQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌟 SparkleQuiz - Learn & Play!")
        self.root.geometry("920x680")
        self.root.configure(bg="#a5f3fc")
        
        self.tracker = QuizTracker()
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🌟 SparkleQuiz", font=("Comic Sans MS", 36, "bold"), bg="#a5f3fc").pack(pady=30)
        tk.Label(self.root, text="Choose a Topic & Test Your Knowledge!", 
                 font=("Arial", 18), bg="#a5f3fc").pack(pady=10)

        topics = get_topics()
        frame = tk.Frame(self.root, bg="#a5f3fc")
        frame.pack(pady=40)

        colors = {"math": "#10b981", "ai": "#3b82f6", "grammar": "#8b5cf6", "software": "#f59e0b"}

        for i, topic in enumerate(topics):
            tk.Button(frame, text=topic.capitalize(), font=("Arial", 16, "bold"),
                      bg=colors.get(topic, "#64748b"), fg="white", width=25, height=3,
                      command=lambda t=topic: self.start_quiz(t)).grid(row=i//2, column=i%2, padx=25, pady=15)

        tk.Button(self.root, text="📊 View My Progress", font=("Arial", 14), bg="#ec4899", fg="white",
                  command=self.show_progress).pack(pady=30)

    def start_quiz(self, topic):
        self.current_topic = topic
        self.questions = get_questions(topic)
        self.current_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        if self.current_index >= len(self.questions):
            self.finish_quiz()
            return

        q = self.questions[self.current_index]
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{self.current_topic.capitalize()} Quiz", 
                 font=("Arial", 20, "bold"), bg="#a5f3fc").pack(pady=10)
        
        tk.Label(self.root, text=q["q"], font=("Arial", 18), bg="#a5f3fc", wraplength=800).pack(pady=40)

        for option in q["options"]:
            tk.Button(self.root, text=option, font=("Arial", 14), bg="#e0f2fe", height=2, width=60,
                      command=lambda ans=option: self.check_answer(ans, q["a"])).pack(pady=8)

    def check_answer(self, selected, correct):
        if selected.lower() == correct.lower():
            self.score += 1
            messagebox.showinfo("✅ Correct!", "Great job!")
        else:
            messagebox.showinfo("😊 Not quite", f"The correct answer is:\n{correct}")

        self.current_index += 1
        self.show_question()

    def finish_quiz(self):
        percentage = self.tracker.record_score(self.current_topic, self.score, len(self.questions))
        messagebox.showinfo("Quiz Complete!", 
            f"You scored {self.score}/{len(self.questions)} ({percentage}%)\n\n"
            f"Keep shining, superstar! 🌟")
        self.create_main_menu()

    def show_progress(self):
        messagebox.showinfo("Progress", "Full progress report coming soon!\n\nWeak topics will be recommended for revision.")

    def run(self):
        self.root.mainloop()