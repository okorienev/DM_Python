from tkinter import Toplevel


class win_3:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry('600x600')
        self.win.resizable(False, False)
        self.win.withdraw()
