from tkinter import Toplevel, Listbox, END, Button, MULTIPLE, Radiobutton, StringVar
from data import *


class Window2:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry("700x600")
        self.win.resizable(False, False)
        self.win.withdraw()
        self.listbox_men = Listbox(self.win, font=20, height=20, selectmod=MULTIPLE)
        for i in male_objects:
            self.listbox_men.insert(END, i.name)
        self.listbox_men.grid(row=1, column=1)
        self.button_add_man = Button(self.win, text='add name', font=20)
        self.button_add_man.grid(row=1, column=2, sticky='n')
        self.listbox_women = Listbox(self.win, font=20, height=20, selectmod=MULTIPLE)
        for i in female_objects:
            self.listbox_women.insert(END, i.name)
        self.listbox_women.grid(row=1, column=3)
        self.button_add_woman = Button(self.win, text='add name', font=20)
        self.button_add_woman.grid(row=1, column=4, sticky='n')
        var = StringVar()
        self.radio1 = Radiobutton(self.win, text='add to A', variable=var, value='A', font=20)
        self.radio1.grid(row=2, column=2)
        self.radio2 = Radiobutton(self.win, text='add to B', variable=var, value='B', font=20)
        self.radio2.grid(row=2, column=3)
