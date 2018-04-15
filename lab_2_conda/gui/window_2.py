from tkinter import Toplevel, Text, Label, Button


class Window2:
    def __init__(self, parent):
        self.win = Toplevel(parent)
        self.win.geometry("650x700")
        self.win.resizable(False, False)
        self.win.withdraw()
        self.label = Label(self.win, text='Structure:', font=20)
        self.label.pack()
        self.label1 = Label(self.win, text='A men&\nA women&\nB men&\nB women', font=20)
        self.label1.pack()
        self.textbox = Text(self.win, width=60, height=20)
        self.textbox.pack()
        self.collect = Button(self.win, font=20, text='collect')
        self.collect.pack()
