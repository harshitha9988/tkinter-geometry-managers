import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = datetime(year, month, day)
        today = datetime.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for date, month, and year.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Enter your Date of Birth", font=("Times New Roman", 14)).pack(pady=10)

tk.Label(root, text="Day").pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Month").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 12))
result_label.pack()

root.mainloop()