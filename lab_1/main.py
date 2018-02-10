from tkinter import Tk, Toplevel, Button, messagebox, filedialog, Menu, Frame, Label, Entry, Text
from webbrowser import open_new
from random import shuffle
from full_calculation import FullCalculation
from simplified_calculation import simplified_calc


def on_closing_root():
    """Handling closing first window by pressing "x"""""
    if messagebox.askokcancel("Quit", "Do you want to quit?", parent=root):
        root.destroy()


def go_to_main():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.withdraw()
    win_5.win.withdraw()


def go_to_win_2():
    win_2.win.deiconify()
    win_3.win.withdraw()
    win_4.win.withdraw()
    win_5.win.withdraw()


def go_to_win_3():
    win_2.win.withdraw()
    win_3.win.deiconify()
    win_4.win.withdraw()
    win_5.win.withdraw()


def go_to_win_4():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.deiconify()
    win_5.win.withdraw()


def go_to_win_5():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.withdraw()
    win_5.win.deiconify()


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
        self.menu.add_command(label='GitHub', font=16,
                              command=lambda: open_new('https://github.com/AlexPraefectus/DM_Python'))
        self.menu.add_command(label='Info', font=16,
                              command=lambda: messagebox.showinfo('Info', 'Oleksandr Korienev, IV-7210'))


class MyWindow:
    def __init__(self):
        self.win = Toplevel()
        self.win.geometry('670x600')
        self.win.resizable(False, False)
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing_win)

    def on_closing_win(self):
        if messagebox.askokcancel('Hide', 'Are you sure?', parent=self.win):
            self.win.withdraw()

a = set()
b = set()
c = set()
u = set()
x = set()
z = set()
operator = None


def generate_sets():
    try:
        global u
        u = {i for i in range(int(u_range_start.get()), int(u_range_stop.get()) + 1)}
        gen_a = list(u.copy())
        gen_b = list(u.copy())
        gen_c = list(u.copy())
        shuffle(gen_a)
        shuffle(gen_b)
        shuffle(gen_c)
        global a, b, c, x, z
        a = {gen_a.pop() for i in range(int(set_a_entry.get()))}
        b = {gen_b.pop() for i in range(int(set_b_entry.get()))}
        c = {gen_c.pop() for i in range(int(set_c_entry.get()))}
        global operator
        operator = FullCalculation(a, b, c, u)
        x = u - c
        z = b
    except ValueError:
        messagebox.showerror('Error', 'Your input can not be processed')


def generate_u():
    try:
        global u
        u = {i for i in range(int(u_range_start.get()), int(u_range_stop.get()) + 1)}
    except ValueError:
        messagebox.showerror('Error', 'Your input can not be processed')


def collect_callback():
    try:
        global a, b, c, x, z, operator
        a = {int(i) for i in a_textbox.get('1.0', 'end-1c').split(',')}
        b = {int(i) for i in b_textbox.get('1.0', 'end-1c').split(',')}
        c = {int(i) for i in c_textbox.get('1.0', 'end-1c').split(',')}
        if not all([(i in u) for i in a]) or not all([(i in u) for i in b]) or not all([(i in u) for i in c]):
            messagebox.showwarning('Warning', 'Your input is out of range of universal set\n'
                                              'Calculations will be incorrect')
        x = u - c
        z = b
        operator = FullCalculation(a, b, c, u)
    except ValueError:
        messagebox.showerror('Error', 'Numbers should be integer, separate values by \',\'')

root = Tk()
root.title("Main Window")
root.geometry("670x600")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing_root)
root_menu = NavMenu()
root.config(menu=root_menu.menu)
#
win_2 = MyWindow()
win_2.win.withdraw()
set_size_frame = Frame(root)
set_a = Label(set_size_frame, text='Size of A', font=16)
set_a.grid(row=1, column=1, sticky='w')
set_a_entry = Entry(set_size_frame, width=4, font=16)
set_a_entry.grid(row=1, column=2)
set_b = Label(set_size_frame, text='Size of B', font=16)
set_b.grid(row=1, column=3)
set_b_entry = Entry(set_size_frame, width=4, font=16)
set_b_entry.grid(row=1, column=4)
set_size_frame.grid(row=1, column=1, columnspan=4)
set_c = Label(set_size_frame, text='Size of C', font=16)
set_c.grid(row=1, column=5)
set_c_entry = Entry(set_size_frame, width=4, font=16)
set_c_entry.grid(row=1, column=6)
u_range = Label(set_size_frame, text='Range of U set', font=16)
u_range.grid(row=1, column=7)
u_range_start = Entry(set_size_frame, width=4, font=16)
u_range_start.grid(row=1, column=8)
symbol = Label(set_size_frame, text=':', font=16)
symbol.grid(row=1, column=9)
u_range_stop = Entry(set_size_frame, width=4, font=16)
u_range_stop.grid(row=1, column=10)
generate = Button(text='generate sets', font=16, width=11, command=generate_sets)
generate.grid(row=1, column=11)
generate_u = Button(text='generate U', font=16, width=11, command=generate_u)
generate_u.grid(row=2, column=11, sticky='e')
set_size_frame.grid(row=1, column=1, sticky='w')

hand_input = Frame(root)
label1 = Label(hand_input, text='A set', font=16)
label1.grid(row=1, column=1, sticky='w')
a_textbox = Text(hand_input, width=60, height=5)
a_textbox.grid(row=2, column=1)
hand_input.grid(row=3, column=1, sticky='w')


label2 = Label(hand_input, text='B set', font=16)
label2.grid(row=3, column=1, sticky='w')
b_textbox = Text(hand_input, width=60, height=5)
b_textbox.grid(row=4, column=1)

label3 = Label(hand_input, text='C set', font=16)
label3.grid(row=5, column=1, sticky='w')
c_textbox = Text(hand_input, width=60, height=5)
c_textbox.grid(row=6, column=1)

collect = Button(text='Collect', font=16, width=8, command=collect_callback)
collect.grid(row=3, column=2, sticky='e')

calculate = Button(text='Calculate', font=16, width=8,
                   command=lambda: messagebox.showinfo('Result', operator.get_result()) if operator else
                   messagebox.showerror('Error', 'Sets-operands are not correct'))
calculate.grid(row=7, column=1, sticky='w')
#
win_3 = MyWindow()
win_3.win.withdraw()
win_4 = MyWindow()
win_4.win.withdraw()
win_5 = MyWindow()
win_5.win.withdraw()


root.mainloop()
