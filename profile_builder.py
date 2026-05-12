# SIMPLE PROFILE BUILDER
# Beginner Student Version

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os

# ---------------- EXCEL FILE ----------------

file_name = "profile.xlsx"

# create excel file if not existing
if os.path.exists(file_name):
    workbook = load_workbook(file_name)

else:
    workbook = Workbook()
    sheet = workbook.active

    # headers
    sheet["A1"] = "ID"
    sheet["B1"] = "Last Name"
    sheet["C1"] = "First Name"
    sheet["D1"] = "Middle Name"
    sheet["E1"] = "Birth Year"
    sheet["F1"] = "Age"

    workbook.save(file_name)

# open excel
workbook = load_workbook(file_name)
sheet = workbook.active

# ----------------
