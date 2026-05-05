import tkinter as tk

root = tk.Tk()
root.title("Password Strength")
root.geometry("300x200")

result = tk.StringVar()

tk.Label(root, text="Enter Password:").pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Label(root, textvariable=result).pack(pady=10)

def check(event):
    password = entry.get()
    length = len(password)

    if length == 0:
        result.set("Please enter a password")
    elif length < 6:
        result.set("Weak")
    elif length < 10:
        result.set("Medium")
    else:
        result.set("Strong")

# Run when Enter key is pressed
entry.bind("<Return>", check)

root.mainloop()