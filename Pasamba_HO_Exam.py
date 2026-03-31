import tkinter as tk

window = tk.Tk()
window.title("Log in System")
window.geometry("300x200")

label = tk.Label(window, text = "Welcome!")
label.pack(pady = 10)

def register ():
   window = tk.Toplevel()
   window.title("Registering")
   window.configure(bg = "green")
   window.geometry("200x100")

   label1 = tk.Label(window, text = "Username", bg = "green")
   label1.grid(row = 2, column = 0)
   label1 = tk.Entry(window,)
   label1.grid(row = 2, column = 1)

   label1 = tk.Label(window, text = "Password", bg = "green")
   label1.grid(row = 3, column = 0)
   label1 = tk.Entry(window,)
   label1.grid(row = 3, column = 1)

   btn = tk.Checkbutton(window, text = "Set Password")
   btn.grid(row = 4, column = 1, columnspan = 2)

   btn1 = tk.Button(window, text = "Register")
   btn1.grid(row = 5, column = 1 , columnspan = 3, rowspan = 5, pady = 10,)

def log_in ():
   window = tk.Toplevel()
   window.title("Registering")
   window.configure(bg = "red")
   window.geometry("200x100")

   label1 = tk.Label(window, text = "Username", bg = "red")
   label1.grid(row = 2, column = 0)
   label1 = tk.Entry(window,)
   label1.grid(row = 2, column = 1)

   label1 = tk.Label(window, text = "Password", bg = "red")
   label1.grid(row = 3, column = 0)
   label1 = tk.Entry(window,)
   label1.grid(row = 3, column = 1)

   btn = tk.Checkbutton(window, text = "Set Password")
   btn.grid(row = 5, column = 1, columnspan = 2)   

btn1 = tk.Button(window, text = "Register", bg = "blue", fg = "black", height = "2", command=register)
btn1.pack(fill="x")
btn1 = tk.Button(window, text = "Log In", bg = "green", fg = "black", height = "2", command=log_in)
btn1.pack(fill="x")

window.mainloop()
