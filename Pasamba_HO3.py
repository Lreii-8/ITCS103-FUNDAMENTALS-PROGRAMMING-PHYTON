import tkinter as tk

window = tk.Tk()
window.title("Calculator Application")
window.geometry("300x200")
window.configure(bg = "#2F4156", cursor = "boat")

la_be_l = tk.Label(window,bg = "#C8D9E6", text="Enter 1st number ")
la_be_l.grid(row=1, column=0)

label_2 = tk.Label(window,bg = "#C8D9E6", text="Enter 2nd number ")
label_2.grid(row=2, column=0)

entry_1 = tk.Entry(window)
entry_1.grid(row=1, column=1)

entry_2 = tk.Entry(window)
entry_2.grid(row=2, column=1)

result = tk.Label(window,bg = "#F0E7D5", text="Result will appear here")
result.grid(row=0, column=0, columnspan=2, pady=10)

def add():
    a = int(entry_1.get())
    b = int(entry_2.get())
    result.config(text="Sum = " + str(a + b))

def sub():
    a = int(entry_1.get())
    b = int(entry_2.get())
    result.config(text="Difference = " + str(a - b))

def mul():
    a = int(entry_1.get())
    b = int(entry_2.get())
    result.config(text="Product = " + str(a * b))

def div():
    a = int(entry_1.get())
    b = int(entry_2.get())
    result.config(text="Quotient = " + str(a / b))

btn1 = tk.Button(window,bg = "#F0E7D5", text="Add", width=10, command=add)
btn1.grid(row=3, column=0, pady=5)
btn2 = tk.Button(window,bg = "#F0E7D5", text="Subtract", width=10, command=sub)
btn2.grid(row=3, column=1)

btn3 = tk.Button(window,bg = "#F0E7D5", text="Multiply", width=10, command=mul)
btn3.grid(row=4, column=0, pady=5)
btn4 = tk.Button(window,bg = "#F0E7D5", text="Division", width=10, command=div)
btn4.grid(row=4, column=1)

window.mainloop()