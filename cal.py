import tkinter as tk

# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x200")

# Labels
label1 = tk.Label(window, text="Enter 1st number")
label1.grid(row=1, column=0)

label2 = tk.Label(window, text="Enter 2nd number")
label2.grid(row=2, column=0)

# Entries
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1)

entry2 = tk.Entry(window)
entry2.grid(row=2, column=1)

# Result label
result = tk.Label(window, text="Result will appear here")
result.grid(row=0, column=0, columnspan=2, pady=10)

# Functions
def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Sum = " + str(a + b))

def sub():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Difference = " + str(a - b))

def mul():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Product = " + str(a * b))

def div():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Quotient = " + str(a / b))

# Buttons
btn1 = tk.Button(window, text="Add", width=10, command=add)
btn1.grid(row=3, column=0, pady=5)

btn2 = tk.Button(window, text="Subtract", width=10, command=sub)
btn2.grid(row=3, column=1)

btn3 = tk.Button(window, text="Multiply", width=10, command=mul)
btn3.grid(row=4, column=0, pady=5)

btn4 = tk.Button(window, text="Division", width=10, command=div)
btn4.grid(row=4, column=1)

# Run program
window.mainloop()
