import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        buttons_frame.pack()
        
        # 1st row
        self.create_button(buttons_frame, "C", 1, 0, "darkorange", lambda: self.clear())
        self.create_button(buttons_frame, "/", 1, 1, "lightgray", lambda: self.click("/"))
        self.create_button(buttons_frame, "*", 1, 2, "lightgray", lambda: self.click("*"))
        self.create_button(buttons_frame, "-", 1, 3, "lightgray", lambda: self.click("-"))
        
        # 2nd row
        self.create_button(buttons_frame, "7", 2, 0, "white", lambda: self.click("7"))
        self.create_button(buttons_frame, "8", 2, 1, "white", lambda: self.click("8"))
        self.create_button(buttons_frame, "9", 2, 2, "white", lambda: self.click("9"))
        self.create_button(buttons_frame, "+", 2, 3, "lightgray", lambda: self.click("+"))
        
        # 3rd row
        self.create_button(buttons_frame, "4", 3, 0, "white", lambda: self.click("4"))
        self.create_button(buttons_frame, "5", 3, 1, "white", lambda: self.click("5"))
        self.create_button(buttons_frame, "6", 3, 2, "white", lambda: self.click("6"))
        self.create_button(buttons_frame, "=", 3, 3, "lightgreen", lambda: self.calculate(), 2)
        
        # 4th row
        self.create_button(buttons_frame, "1", 4, 0, "white", lambda: self.click("1"))
        self.create_button(buttons_frame, "2", 4, 1, "white", lambda: self.click("2"))
        self.create_button(buttons_frame, "3", 4, 2, "white", lambda: self.click("3"))
        
        # 5th row
        self.create_button(buttons_frame, "0", 5, 0, "white", lambda: self.click("0"), 2)
        self.create_button(buttons_frame, ".", 5, 2, "white", lambda: self.click("."))
    
    def create_button(self, frame, text, row, column, color, command, rowspan=1, columnspan=1):
        button = tk.Button(frame, text=text, fg="black", width=10, height=3, bd=0, bg=color, cursor="hand2", command=command)
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=1, pady=1)

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
        
    def clear(self):
        self.expression = ""
        self.input_text.set("")
        
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Error en la expresión")
            self.expression = ""
            self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
