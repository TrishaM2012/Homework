import tkinter as tk

def calculate_age():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())

    current_day = 15
    current_month = 4
    current_year = 2026
    age = current_year - year

    if (current_month < month) or (current_month == month and current_day < day):
        age -= 1

    result_label.config(text=f"Your age is: {age} years")


root = tk.Tk()
root.title("Age Calculator (No datetime)")
root.geometry("320x250")

tk.Label(root, text="Day").pack()
entry_day = tk.Entry(root)
entry_day.pack()

tk.Label(root, text="Month").pack()
entry_month = tk.Entry(root)
entry_month.pack()

tk.Label(root, text="Year").pack()
entry_year = tk.Entry(root)
entry_year.pack()
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()