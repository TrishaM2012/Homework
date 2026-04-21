import tkinter as tk
from tkinter import messagebox

def converter():
    inches = float(entry.get())
    result = inches * 2.54
    messagebox.showinfo("Result = ", str(result)+" cm")

root = tk.Tk()
root.title("Length Calculator App")
root.geometry("400x400")
label = tk.Label(root, text="Enter length in inches:")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
convert_button = tk.Button(root, text="Convert", command=converter)
convert_button.pack(pady=5)

root.mainloop()
