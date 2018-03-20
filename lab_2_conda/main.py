from tkinter import Tk, Menu, Button,Listbox, Radiobutton, messagebox, END
from webbrowser import open_new
from gui.window_2 import Window2 as Win2
from gui.window_3 import win_3 as Win3
from gui.window_4 import Window4 as Win4
from logic.graph import GraphDrawer
from data import male_objects, female_objects
from itertools import chain
from random import choice
from logic.genders import Male, Female

A = set()
B = set()


def go_to_main():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.withdraw()


def go_to_win_2():
    win_2.win.deiconify()
    win_3.win.withdraw()
    win_4.win.withdraw()


def go_to_win_3():
    win_2.win.withdraw()
    win_3.win.deiconify()
    win_4.win.withdraw()


def go_to_win_4():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.deiconify()


def add_man_callback(event):
    global A, B
    for i in win_2.listbox_men.curselection():
        if win_2.var.get() == 'A':
            A.add(Male(win_2.listbox_men.get(i)))
            win_2.listbox_a.insert(END, win_2.listbox_men.get(i))
        elif win_2.var.get() == 'B':
            B.add(Male(win_2.listbox_men.get(i)))
            win_2.listbox_b.insert(END, win_2.listbox_men.get(i))
    print(A, B)


def add_woman_callback(event):
    global A, B
    # print(win_2.var.get(), win_2.listbox_men.curselection())
    for i in win_2.listbox_women.curselection():
        if win_2.var.get() == 'A':
            A.add(Female(win_2.listbox_women.get(i)))
            win_2.listbox_a.insert(END, win_2.listbox_women.get(i))
        elif win_2.var.get() == 'B':
            B.add(Female(win_2.listbox_women.get(i)))
            win_2.listbox_b.insert(END, win_2.listbox_women.get(i))
    print(A, B)


def default_graph(event):
    a = {choice(list(chain(male_objects, female_objects))) for i in range(10)}
    b = {choice(list(chain(male_objects, female_objects))) for i in range(10)}
    graph = GraphDrawer(a, b)
    graph.draw_graph_mother()
    graph.draw_graph_mother_in_law()


class NavMenu:
    def __init__(self):
        self.navmenu = Menu()
        self.navmenu.add_command(label='Main Window', font=16, command=go_to_main)
        self.navmenu.add_command(label='Window 2', font=16, command=go_to_win_2)
        self.navmenu.add_command(label='Window 3', font=16, command=go_to_win_3)
        self.navmenu.add_command(label='Window 4', font=16, command=go_to_win_4)
        self.menu = Menu()
        self.menu.add_cascade(label='Navigation', font=16, menu=self.navmenu)
        self.menu.add_command(label='GitHub', font=16,
                              command=lambda: open_new('https://github.com/AlexPraefectus/DM_Python'))
        self.menu.add_command(label='Info', font=16,
                              command=lambda: messagebox.showinfo('Info', 'Oleksandr Korienev, IV-7210\nVariant №23'))

root = Tk()
root_menu = NavMenu()
root.config(menu=root_menu.menu)
default_graph_button = Button(root, text='draw \ndefault\n graphs', font=20, width=15, height=10)
default_graph_button.bind('<Button-1>', default_graph)
default_graph_button.pack()
root.geometry('600x600')

win_2 = Win2(root)
win_2.win.config(menu=NavMenu().menu)
win_2.button_add_man.bind('<Button-1>', add_man_callback)
win_2.button_add_woman.bind('<Button-1>', add_woman_callback)

win_3 = Win3(root)
win_3_menu = NavMenu()
win_3.win.config(menu=win_3_menu.menu)

win_4 = Win4(root)
win_4.win.config(menu=NavMenu().menu)

root.mainloop()
