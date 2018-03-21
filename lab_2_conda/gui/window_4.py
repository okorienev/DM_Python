from tkinter import Toplevel, Button


class Window4:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry('600x600')
        self.win.resizable(False, False)
        self.win.withdraw()
        self.but_intersection = Button(self.win, text='show intersection', font=20)
        self.but_intersection.grid(row=1, column=1, sticky='w')
        self.but_union = Button(self.win, text='show union', font=20)
        self.but_union.grid(row=2, column=1, sticky='w')
        self.but_dif1 = Button(self.win, text=r'show R\S', font=20)
        self.but_dif1.grid(row=3, column=1, sticky='w')
        self.but_dif2 = Button(self.win, text=r'show U\S', font=20)
        self.but_dif2.grid(row=4, column=1, sticky='w')
        self.but_reversed = Button(self.win, text='show reversed r', font=20)
        self.but_reversed.grid(row=5, column=1, sticky='w')
