from tkinter import Toplevel, Listbox, Button


class Window3:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry('600x600')
        self.win.resizable(False, False)
        self.win.withdraw()
        self.a_set_list = Listbox(self.win, font=20)
        self.a_set_list.grid(row=1, column=1, sticky='w')
        self.a_show_but = Button(self.win, text='show a', font=20, width=6)
        self.a_show_but.grid(row=1, column=2, sticky='w')
        self.b_set_list = Listbox(self.win, font=20)
        self.b_set_list.grid(row=1, column=3, sticky='w')
        self.b_show_but = Button(self.win, text='show b', font=20, width=6)
        self.b_show_but.grid(row=1, column=4, sticky='w')
        self.draw_s = Button(self.win, text='draw S relation', font=20)
        self.draw_s.grid(row=2, column=1, sticky='w')
        self.draw_r = Button(self.win, text='draw R relation', font=20)
        self.draw_r.grid(row=2, column=3, sticky='w')
