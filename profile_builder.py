# Simple Profile Builder with Excel
# Install openpyxl first:
# pip install openpyxl

import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os

# ---------------- EXCEL FILE ----------------
file_name = "profiles.xlsx"

# create excel file if not existing
if not os.path.exists(file_name):
    wb = Workbook()
    sheet = wb.active

    headers = ["ID", "Last Name", "First Name", "Middle Name", "Birth Year", "Age"]
    sheet.append(headers)

    wb.save(file_name)

# load workbook
workbook = load_workbook(file_name)
sheet = workbook.active

# ---------------- FUNCTIONS ----------------

def display():
    # clear table
    for row in table.get_children():
        table.delete(row)

    # display excel data
    for row in sheet.iter_rows(min_row=2, values_only=True):
        table.insert("", tk.END, values=row)


def submit():

    fname = first_name_entry.get()
    mname = middle_name_entry.get()
    lname = last_name_entry.get()
    birth = birth_year_entry.get()

    # validation
    if fname == "" or lname == "" or birth == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    age = datetime.now().year - int(birth)

    # auto id
    new_id = sheet.max_row

    # save to excel
    sheet.append([new_id, lname, fname, mname, birth, age])
    workbook.save(file_name)

    messagebox.showinfo("Success", "Saved Successfully")

    # clear entries
    first_name_entry.delete(0, tk.END)
    middle_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    birth_year_entry.delete(0, tk.END)

    display()


def delete_data():

    selected = table.focus()

    if not selected:
        return

    data = table.item(selected)["values"]

    row_id = data[0]

    sheet.delete_rows(row_id + 1)
    workbook.save(file_name)

    display()


# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("Age Calculator")
window.geometry("1000x500")
window.configure(bg="lightgreen")

# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="Profile Builder",
    font=("Times New Roman", 18, "bold"),
    bg="lightgreen"
)
title.pack(pady=10)

# ---------------- FORM FRAME ----------------

form_frame = tk.Frame(window, bg="lightgreen")
form_frame.pack()

# first name
first_name_entry = tk.Entry(form_frame, width=25)
first_name_entry.grid(row=0, column=0, padx=5)

tk.Label(
    form_frame,
    text="First Name",
    bg="lightgreen"
).grid(row=1, column=0)

# middle name
middle_name_entry = tk.Entry(form_frame, width=25)
middle_name_entry.grid(row=0, column=1, padx=5)

tk.Label(
    form_frame,
    text="Middle Name",
    bg="lightgreen"
).grid(row=1, column=1)

# last name
last_name_entry = tk.Entry(form_frame, width=25)
last_name_entry.grid(row=0, column=2, padx=5)

tk.Label(
    form_frame,
    text="Last Name",
    bg="lightgreen"
).grid(row=1, column=2)

# birth year
birth_year_entry = tk.Entry(form_frame, width=25)
birth_year_entry.grid(row=2, column=0, pady=10)

tk.Label(
    form_frame,
    text="Birth Year",
    bg="lightgreen"
).grid(row=3, column=0)

# ---------------- BUTTONS ----------------

button_frame = tk.Frame(window, bg="lightgreen")
button_frame.pack(pady=10)

submit_btn = tk.Button(
    button_frame,
    text="Submit",
    bg="pink",
    command=submit
)
submit_btn.grid(row=0, column=0, padx=20)

update_btn = tk.Button(
    button_frame,
    text="Update",
    bg="lightgray"
)
update_btn.grid(row=0, column=1, padx=20)

delete_btn = tk.Button(
    button_frame,
    text="Delete",
    bg="red",
    fg="white",
    command=delete_data
)
delete_btn.grid(row=0, column=2, padx=20)

# ---------------- TABLE ----------------

columns = ("ID", "Last Name", "First Name", "Middle Name", "Birth Year", "Age")

table = ttk.Treeview(window, columns=columns, show="headings", height=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=140)

table.pack(fill="both", expand=True)

# display data
display()

window.mainloop()
