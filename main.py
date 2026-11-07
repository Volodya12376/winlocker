from tkinter import *
import time
import os

root = Tk()
root.title("WinLock")
root.attributes("-topmost", True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry(f"{w}x{h}")
root.configure(bg="red")

def Quit():
    pass

root.protocol("WM_DELETE_WINDOW", Quit)
root.attributes("-fullscreen", True)

root.mainloop()