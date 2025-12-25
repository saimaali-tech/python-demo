import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Display
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(expand=True, fill="both")
        
        self.input_field = tk.Entry(self.display_frame, textvariable=self.input_text, font=('Arial', 24), bd=0, insertwidth=4, width=14, justify='right')
        self.input_field.pack(expand=True, fill="both", ipadx=10, ipady=10)
        
        # Buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill="both")
        
        buttons = [
            ['7', '8', '9', '/', 'sin', 'asin'],
            ['4', '5', '6', '*', 'cos', 'acos'],
            ['1', '2', '3', '-', 'tan', 'atan'],
            ['0', '.', '(', '+', 'log', 'ln'],
            [')', 'C', '=', '**', 'sqrt', 'exp'],
            ['pi', 'e', 'abs', '%', 'factorial', 'deg'],
            ['rad', 'DEL', '', '', '', '']
        ]
        
        for row in buttons:
            frame = tk.Frame(self.buttons_frame)
            frame.pack(expand=True, fill="both")
            for button in row:
                if button:
                    btn = tk.Button(frame, text=button, font=('Arial', 18), command=lambda b=button: self.button_click(b))
                    btn.pack(side="left", expand=True, fill="both")
        
        # Style the buttons
        self.root.configure(bg="#f0f0f0")
        self.input_field.configure(bg="#ffffff", fg="#000000")
        
    def button_click(self, button):
        if button == '=':
            self.calculate()
        elif button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == 'DEL':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif button in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln', 'sqrt', 'exp', 'abs', 'factorial', 'deg', 'rad']:
            self.expression += f"math.{button}(" if button not in ['deg', 'rad'] else f"math.{button}("
            self.input_text.set(self.expression)
        elif button == 'pi':
            self.expression += "math.pi"
            self.input_text.set(self.expression)
        elif button == 'e':
            self.expression += "math.e"
            self.input_text.set(self.expression)
        elif button == '**':
            self.expression += "**"
            self.input_text.set(self.expression)
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": {}}, {"math": math})
            self.input_text.set(result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""
            self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()