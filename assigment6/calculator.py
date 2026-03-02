from tkinter import *

#  WINDOW
window = Tk()
window.title("Calculator")
window.geometry("350x400")

# ENTRY 
e = Entry(window, width=25, borderwidth=5, font=("Arial", 16))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# GLOBAL VARIABLES 
first_number = None
operator = None

# FUNCTIONS 

def click(value):
    e.insert(END, str(value))

def clear():
    global first_number, operator
    e.delete(0, END)
    first_number = None
    operator = None

def set_operator(op):
    global first_number, operator
    try:
        first_number = float(e.get())
        operator = op
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

def equal():
    global first_number, operator
    try:
        second_number = float(e.get())
        e.delete(0, END)

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                raise ZeroDivisionError
            result = first_number / second_number
        else:
            e.insert(0, "Error")
            return

        e.insert(0, result)

    except ZeroDivisionError:
        e.insert(0, "Cannot divide by 0")

    except:
        e.insert(0, "Error")

# ---------------- BUTTONS ----------------

buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2),
    ('4',2,0), ('5',2,1), ('6',2,2),
    ('7',3,0), ('8',3,1), ('9',3,2),
    ('0',4,1)
]

for (text,row,col) in buttons:
    Button(window, text=text, width=8, height=2,
           command=lambda t=text: click(t)).grid(row=row, column=col)

# Operators
Button(window, text="+", width=8, height=2,
       command=lambda: set_operator("+")).grid(row=1, column=3)

Button(window, text="-", width=8, height=2,
       command=lambda: set_operator("-")).grid(row=2, column=3)

Button(window, text="*", width=8, height=2,
       command=lambda: set_operator("*")).grid(row=3, column=3)

Button(window, text="/", width=8, height=2,
       command=lambda: set_operator("/")).grid(row=4, column=3)

# Equal & Clear
Button(window, text="=", width=8, height=2,
       command=equal).grid(row=4, column=2)

Button(window, text="Clear", width=8, height=2,
       command=clear).grid(row=4, column=0)

#  START 
window.mainloop()