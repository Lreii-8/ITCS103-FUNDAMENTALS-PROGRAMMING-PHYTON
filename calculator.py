import tkinter as tk

def calculate():
    a = float(e1.get())
    b = float(e2.get())
    result.config(text=a + b)

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="Number 1").grid(row=0, column=0)
tk.Label(root, text="Number 2").grid(row=1, column=0)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, text="Add", command=calculate).grid(row=2, column=0, columnspan=2)

result = tk.Label(root, text="Answer")
result.grid(row=3, column=0, columnspan=2)

root.mainloop()
