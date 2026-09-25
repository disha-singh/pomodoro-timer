import tkinter as tk

remaining = 10

def tick():
    global remaining
    label.config(text=str(remaining))
    remaining -= 1
    if remaining >= 0:
        root.after(1000, tick)

root = tk.Tk()
label = tk.Label(root, text = "10", font = ("Airel", 40))
label.pack()

tick()
root.mainloop()