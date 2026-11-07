from tkinter import *
import time
import os

WHITE = "white"
RED = "red"
BLACK = "black"
BLUE = "blue"

root = Tk()
root.title("WinLock")
root.attributes("-topmost", True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry(f"{w}x{h}")
root.configure(bg=BLACK)
Label(
    text="Booting windows...",
    font=("Courier New", 16, "bold"),
    fg=RED,
).pack(pady=(10, 20))

def Quit():
    pass

root.protocol("WM_DELETE_WINDOW", Quit)
root.attributes("-fullscreen", True)

root.mainloop()