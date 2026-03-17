import tkinter as tk

window = tk.Tk()
window.title("title")
window.geometry("400x300")
window.configure(bg = "green")

title = tk.Label(window, text = "Profile Builder", bg = "green", font = ("Roman", 18, "bold"))
title.grid(row=0,column=0)

frame = tk.Frame(window, bg = "lightblue", width = 50)
frame.grid(padx = 10)

#entry
name = tk.Label(frame, text = "First name", bg = "lightblue")
name.grid(row = 2, column = 0, pady = 5)
enter1 = tk.Entry(frame, width = 19 )
enter1.grid(row = 1, column = 0 )
name = tk.Label(frame, text = "Middle Name", bg = "lightblue")
name.grid(row = 2, column = 1, pady = 5)
enter2 = tk.Entry(frame,)
enter2.grid(row = 1, column = 1)
name = tk.Label(frame, text = "Last Name", bg = "lightblue")
name.grid(row = 2, column = 2, pady = 5)
enter3 = tk.Entry(frame, width = 19 )
enter3.grid(row = 1, column = 2)
name = tk.Label(frame, text = "Birth Year", bg = "lightblue")
name.grid(row = 4, column = 0)
enter4 = tk.Entry(frame)
enter4.grid(row = 3, column = 0)
name = tk.Label(frame, text = "Gender", bg = "lightblue")
name.grid(row = 5, column = 0)

#check button
btn = tk.Checkbutton(frame, text = "Male", bg = "lightblue")
btn.grid(row = 5, column = 1)
btn = tk.Checkbutton(frame, text = "female", bg = "lightblue")
btn.grid(row = 5, column = 2)

btn_1 = tk.Button(window, text = "Sumbit", bg = "lightblue")
btn_1.grid(row = 6, column = 0,)






window.mainloop()
