import tkinter as tk

def calculate():
    if e1.get() and e2.get() and e3.get():
        p = float(e1.get())
        r = float(e2.get())
        t = float(e3.get())

        si = (p * r * t) / 100
        ci = p * (1 + r/100) ** t - p

        si_label.config(text="Simple Interest: " + str(round(si, 2)))
        ci_label.config(text="Compound Interest: " + str(round(ci, 2)))

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Rate").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Time").pack()
e3 = tk.Entry(root)
e3.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

si_label = tk.Label(root, text="")
si_label.pack()

ci_label = tk.Label(root, text="")
ci_label.pack()

root.mainloop()
