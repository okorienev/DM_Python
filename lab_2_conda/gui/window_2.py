from tkinter import Toplevel, Listbox, END, Button, MULTIPLE, Radiobutton, StringVar, Text, Label
from data import *


class Window2:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry("650x700")
        self.win.resizable(False, False)
        self.win.withdraw()
        # self.listbox_men = Listbox(self.win, font=20, height=20, selectmod=MULTIPLE)
        # for i in male_objects:
        #     self.listbox_men.insert(END, i.name)
        # self.listbox_men.grid(row=1, column=1)
        # self.button_add_man = Button(self.win, text='add name', font=20)
        # self.button_add_man.grid(row=1, column=2, sticky='n')
        # self.listbox_women = Listbox(self.win, font=20, height=20, selectmod=MULTIPLE)
        # for i in female_objects:
        #     self.listbox_women.insert(END, i.name)
        # self.listbox_women.grid(row=1, column=3)
        # self.button_add_woman = Button(self.win, text='add name', font=20)
        # self.button_add_woman.grid(row=1, column=4, sticky='n')
        # self.var = StringVar()
        # self.radio1 = Radiobutton(self.win, text='add to A', variable=self.var, value='A', font=20)
        # self.radio1.grid(row=2, column=2)
        # self.radio2 = Radiobutton(self.win, text='add to B', variable=self.var, value='B', font=20)
        # self.radio2.grid(row=2, column=3)
        # self.listbox_a = Listbox(self.win, height=15, font=20)
        # self.listbox_a.grid(row=3, column=1)
        # self.listbox_b = Listbox(self.win, height=15, font=20)
        # self.listbox_b.grid(row=3, column=3)
        # self.button_save = Button(self.win, text='save to file', width=15, font=20)
        # self.button_save.grid(row=4, column=1, sticky='w')
        # self.button_read = Button(self.win, text='read from file', width=15, font=20)
        # self.button_read.grid(row=4, column=3, sticky='w')
        # self
        self.label = Label(self.win, text='Structure:', font=20)
        self.label.pack()
        self.label1 = Label(self.win, text='A men&\nA women&\nB men&\nB women', font=20)
        self.label1.pack()
        self.textbox = Text(self.win, width=60, height=20)
        self.textbox.pack()
        self.collect = Button(self.win, font=20, text='collect')
        self.collect.pack()
