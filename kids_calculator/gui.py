import tkinter as tk
from tkinter import messagebox
from .core import Calculator

class CalculatorGUI:
    def __init__(self):
        self.calc = Calculator()
        self.root = tk.Tk()
        self.root.title("🧠 Kids Math Calculator")
        self.root.geometry("700x850")
        self.root.configure(bg="#f0f8ff")

        self.display = tk.Entry(self.root, font=("Arial", 34, "bold"), justify="right", bd=15, relief="sunken", bg="white")
        self.display.grid(row=0, column=0, columnspan=5, padx=25, pady=40, sticky="ew")

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f8ff")
        btn_frame.grid(row=1, column=0, columnspan=5, padx=20, pady=10)

        def btn(text, r, c, color="#f8f9fa", span=1, cmd=None):
            tk.Button(btn_frame, text=text, font=("Arial", 18, "bold"), bg=color, height=2,
                      command=cmd or (lambda: self.click(text))).grid(row=r, column=c, columnspan=span, padx=5, pady=5, sticky="nsew")

        buttons = [
            ("C", 0, 0, "#ff6b6b"), ("(", 0, 1), (")", 0, 2), ("/", 0, 3, "#ffd166"),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3, "#ffd166"),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3, "#ffd166"),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3, "#ffd166"),
            ("0", 4, 0, "#f1f5f9", 2), (".", 4, 2), ("=", 4, 3, "#06d6a0", 1, 2),
            ("sin", 5, 0, "#bae6fd"), ("cos", 5, 1, "#bae6fd"), ("tan", 5, 2, "#bae6fd"),
        ]

        for b in buttons:
            btn(*b)

        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.mainloop()

    def click(self, value):
        if value == "=":
            self.calculate()
        elif value == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)

    def calculate(self):
        expr = self.display.get().strip()
        if not expr:
            return
        try:
            result = self.calc.calculate(expr)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except ValueError as e:
            messagebox.showerror("Oops!", str(e))
            self.display.delete(0, tk.END)

if __name__ == "__main__":
    CalculatorGUI()