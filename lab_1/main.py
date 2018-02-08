from tkinter import Tk, Toplevel, Button, messagebox, filedialog, Menu


def on_closing_root():
    """Handling closing first window by pressing "x"""""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def go_to_main():
    win_2.withdraw()
    win_3.withdraw()
    win_4.withdraw()
    win_5.withdraw()


def go_to_win_2():
    win_2.deiconify()
    win_3.withdraw()
    win_4.withdraw()
    win_5.withdraw()


def go_to_win_3():
    win_2.withdraw()
    win_3.deiconify()
    win_4.withdraw()
    win_5.withdraw()


def go_to_win_4():
    win_2.withdraw()
    win_3.withdraw()
    win_4.deiconify()
    win_5.withdraw()


def go_to_win_5():
    win_2.withdraw()
    win_3.withdraw()
    win_4.withdraw()
    win_5.deiconify()


class NavMenu:
    def __init__(self):
        self.navmenu = Menu()
        self.navmenu.add_command(label='Main Window', font=16, command=go_to_main)
        self.navmenu.add_command(label='Window 2', font=16, command=go_to_win_2)
        self.navmenu.add_command(label='Window 3', font=16, command=go_to_win_3)
        self.navmenu.add_command(label='Window 4', font=16, command=go_to_win_4)
        self.navmenu.add_command(label='Window 5', font=16, command=go_to_win_5)
        self.menu = Menu()
        self.menu.add_cascade(label='Navigation', font=16, menu=self.navmenu)


a = set()
b = set()
c = set()
u = set()
x = set()
z = set()

root = Tk()
root.title("Main Window")
root.geometry("670x600")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing_root)
root_menu = NavMenu()
root.config(menu=root_menu.menu)
win_2 = Toplevel()
win_2.withdraw()
win_3 = Toplevel()
win_3.withdraw()
win_4 = Toplevel()
win_4.withdraw()
win_5 = Toplevel()
win_5.withdraw()


root.mainloop()
