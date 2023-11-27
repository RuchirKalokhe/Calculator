import tkinter as tk
from tkinter import *
from math import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")
        self.root.geometry("380x800")
        self.root.configure(bg="#333")

        self.entry_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.entry_var, width=30, font=('Smooch Sans Bold', 20), bd=25, relief="ridge", justify="right", bg="#444", fg="white")  
        entry.grid(row=0, column=0, rowspan=1, columnspan=4)

        buttons = [
            ('%', self.percent),
            ('CE', self.clear_entry),
            ('C', self.clear_all),
            ('<-', self.backspace),
            ('1/x', self.reciprocal), 
            ('^', lambda: self.append_to_entry('**')),
            ('sqrt', self.square_root),
            ('/', lambda: self.append_to_entry('/')),
            ('7', lambda: self.append_to_entry('7')),
            ('8', lambda: self.append_to_entry('8')),
            ('9', lambda: self.append_to_entry('9')),
            ('*', lambda: self.append_to_entry('*')),
            ('4', lambda: self.append_to_entry('4')),
            ('5', lambda: self.append_to_entry('5')),
            ('6', lambda: self.append_to_entry('6')),
            ('-', lambda: self.append_to_entry('-')),
            ('1', lambda: self.append_to_entry('1')),
            ('2', lambda: self.append_to_entry('2')),
            ('3', lambda: self.append_to_entry('3')),
            ('+', lambda: self.append_to_entry('+')),
            ('+/-', self.negate),
            ('0', lambda: self.append_to_entry('0')),
            ('.', lambda: self.append_to_entry('.')),
            ('=', self.calculate_result),
        ]

        # Create and place buttons
        rv = 1
        cv = 0
        for (text, command) in buttons:
            tk.Button(root, text=text, width=7, height=2, font=('Smooch Sans Bold', 25), command=command, bg="#282A36", fg="white").grid(row=rv, column=cv)
            cv += 1
            if cv > 3:
                cv = 0
                rv += 1

        # Configure row and column weights
        for i in range(1, 5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def append_to_entry(self, value):
        current_text = self.entry_var.get()
        self.entry_var.set(current_text + value)
#-----------------------------------------------
    def clear_entry(self):
        self.entry_var.set("")
#-----------------------------
    def clear_all(self):
        self.clear_entry()
#-------------------------
    def backspace(self):
        current_text = self.entry_var.get()
        self.entry_var.set(current_text[:-1])
#--------------------------------------------
    def negate(self):
        current_text = self.entry_var.get()
        if current_text and current_text[0] == '-':
            self.entry_var.set(current_text[1:])
        else:
            self.entry_var.set('-' + current_text)
#--------------------------------------------------
    def square_root(self):
        current_text = self.entry_var.get()
        try:
            result = sqrt(eval(current_text))
            self.entry_var.set(result)
        except Exception as e:
            self.entry_var.set("Error")
#---------------------------------------------
    def percent(self):
        current_text = self.entry_var.get()
        try:
            result = eval(current_text) / 100
            self.entry_var.set(result)
        except Exception as e:
            self.entry_var.set("Error")
#--------------------------------------------
    def reciprocal(self):
        current_text = self.entry_var.get()
        try:
            result = 1 / eval(current_text)
            self.entry_var.set(result)
        except Exception as e:
            self.entry_var.set("Error")
#------------------------------------------
    def calculate_result(self):
        current_text = self.entry_var.get()
        try:
            result = eval(current_text)
            self.entry_var.set(result)
        except Exception as e:
            self.entry_var.set("Error")
#------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()