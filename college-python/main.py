from tkinter import *
from tkinter import ttk

clicks = 0

root = Tk()

root.title("Gui python")

root.geometry("300x400")

def btnClick():
    global clicks
    clicks += 1
    btn["text"] = f"Clicks {clicks}"


btn = ttk.Button(text="But", command=btnClick)


btn.pack()


root.mainloop()
