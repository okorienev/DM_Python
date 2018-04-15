from tkinter import Tk, Toplevel, Button, messagebox, filedialog, Menu, Frame, Label, Entry, Text, END
from webbrowser import open_new
from random import shuffle
from full_calculation import FullCalculation
from simplified_calculation import SimplifiedCalculation
import subprocess as sp
import csv


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
                              command=lambda: messagebox.showinfo('Info', 'Oleksandr Korienev, IV-7210\nVariant №23'))


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
y = set()
operator = None
operator_s = None


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
        global a, b, c, x, y
        a = {gen_a.pop() for i in range(int(set_a_entry.get()))}
        b = {gen_b.pop() for i in range(int(set_b_entry.get()))}
        c = {gen_c.pop() for i in range(int(set_c_entry.get()))}
        global operator, operator_s
        operator = FullCalculation(a, b, c, u)
        operator_s = SimplifiedCalculation(a, b, c, u)
        x = u - c
        y = b
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
        global a, b, c, x, y, operator, operator_s
        a = {int(i) for i in a_textbox.get('1.0', 'end-1c').split(',')}
        b = {int(i) for i in b_textbox.get('1.0', 'end-1c').split(',')}
        c = {int(i) for i in c_textbox.get('1.0', 'end-1c').split(',')}
        if not all([(i in u) for i in a]) or not all([(i in u) for i in b]) or not all([(i in u) for i in c]):
            messagebox.showwarning('Warning', 'Your input is out of range of universal set\n'
                                              'Calculations will be incorrect')
        x = u - c
        y = b
        operator = FullCalculation(a, b, c, u)
        operator_s = SimplifiedCalculation(a, b, c, u)
    except ValueError:
        messagebox.showerror('Error', 'Numbers should be integer, separate values by \',\'')


def read_from_csv():
    try:
        with open(filedialog.askopenfilename(title="Select csv file", filetypes=[('csv files', '*.csv')])) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            data = [[int(i) for i in row] for row in reader]
            global u, a, b, c, x, y, operator, operator_s
            u = {i for i in range(data[0][0], data[0][1] + 1)}
            a = set(data[1])
            b = set(data[2])
            c = set(data[3])
            if not all([i in u for i in a.union(b).union(c)]):
                messagebox.showwarning('Warning', 'Numbers are out of universal set range')
            operator = FullCalculation(a, b, c, u)
            operator_s = SimplifiedCalculation(a, b, c, u)
            x = u - c
            y = b
    except TypeError:
        messagebox.showerror('Error', 'Wrong file')
    except FileNotFoundError:
        messagebox.showerror('Error', 'File wasn\'t chosen')
    except ValueError:
        messagebox.showerror('Error', 'Data format incorrect')
        messagebox.showinfo('Info', 'Data format:\nint,int - range of u set\nint,...,int - data strings(3 times)')


def show_a_callback():
    text_field.delete(1.0, END)
    text_field.insert(1.0, a)


def show_b_callback():
    text_field.delete(1.0, END)
    text_field.insert(1.0, b)


def show_c_callback():
    text_field.delete(1.0, END)
    text_field.insert(1.0, c)


def step_1_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nunion with\n{}\nresult:\n{}".format(' '.join(map(str, operator.A)),
                                                                        ' '.join(map(str, operator.B)),
                                                                        ' '.join(map(str, operator.step_1()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_2_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nunion with\n{}\nresult:\n{}".format(' '.join(map(str, operator.A)),
                                                                        ' '.join(map(str, operator.U - operator.B)),
                                                                        ' '.join(map(str, operator.step_2()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_3_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nunion with\n{}\nresult:\n{}".format(' '.join(map(str, operator.U - operator.A)),
                                                                        ' '.join(map(str, operator.C)),
                                                                        ' '.join(map(str, operator.step_3()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_4_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nunion with\n{}\nresult:\n{}".format(' '.join(map(str, operator.step_1())),
                                                                        ' '.join(map(str, operator.step_2())),
                                                                        ' '.join(map(str, operator.step_4()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_5_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nintersects\n{}\nresult:\n{}".format(' '.join(map(str, operator.step_4())),
                                                                        ' '.join(map(str, operator.U - operator.B)),
                                                                        ' '.join(map(str, operator.step_5()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_6_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nintersects\n{}\nresult:\n{}".format(' '.join(map(str, operator.step_5())),
                                                                        ' '.join(map(str, operator.A)),
                                                                        ' '.join(map(str, operator.step_6()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_7_callback():
    try:
        text_field.delete(1.0, END)
        text_field.insert(1.0, "{}\nintersects\n{}\nresult:\n{}".format(' '.join(map(str, operator.step_6())),
                                                                        ' '.join(map(str, operator.step_3())),
                                                                        ' '.join(map(str, operator.get_result()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_1_s_callback():
    try:
        text_field_n.delete(1.0, END)
        text_field_n.insert(1.0, "{}\nintersects\n{}\nresult:\n{}".format(' '.join(map(str, operator_s.u - operator_s.b)),
                                                                        ' '.join(map(str, operator_s.a)),
                                                                        ' '.join(map(str, operator_s.step_1()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def step_2_s_callback():
    try:
        text_field_n.delete(1.0, END)
        text_field_n.insert(1.0, "{}\nintersects\n{}\nresult:\n{}".format(' '.join(map(str, operator_s.step_1())),
                                                                        ' '.join(map(str, operator_s.c)),
                                                                        ' '.join(map(str, operator_s.get_result()))))
    except AttributeError:
        messagebox.showerror('Error', 'operator object is not initialized, please generate or collect the operand sets')


def show_a_w3_callback():
    text_field_n.delete(1.0, END)
    text_field_n.insert(1.0, a)


def show_b_w3_callback():
    text_field_n.delete(1.0, END)
    text_field_n.insert(1.0, b)


def show_c_w3_callback():
    text_field_n.delete(1.0, END)
    text_field_n.insert(1.0, c)


def show_x_callback():
    text_field_4.delete(1.0, END)
    text_field_4.insert(1.0, x)


def show_y_callback():
    text_field_4.delete(1.0, END)
    text_field_4.insert(1.0, y)


def calculate_z_callback():
    text_field_4.delete(1.0, END)
    text_field_4.insert(1.0, y.union(x))


def run_unittest_callback():
    p = sp.Popen(['python3', 'testing.py'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, errors = p.communicate()
    text_field_4.delete(1.0, END)
    text_field_4.insert(1.0, output + errors)


root = Tk()
root.title("Main Window")
root.geometry("670x600")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing_root)
root_menu = NavMenu()
root.config(menu=root_menu.menu)
#
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
#
hand_input = Frame(root)
label1 = Label(hand_input, text='A set', font=16)
label1.grid(row=1, column=1, sticky='w')
a_textbox = Text(hand_input, width=60, height=5)
a_textbox.grid(row=2, column=1)
hand_input.grid(row=3, column=1, sticky='w')
#
label2 = Label(hand_input, text='B set', font=16)
label2.grid(row=3, column=1, sticky='w')
b_textbox = Text(hand_input, width=60, height=5)
b_textbox.grid(row=4, column=1)
#
label3 = Label(hand_input, text='C set', font=16)
label3.grid(row=5, column=1, sticky='w')
c_textbox = Text(hand_input, width=60, height=5)
c_textbox.grid(row=6, column=1)
#
collect = Button(text='Collect', font=16, width=8, command=collect_callback)
collect.grid(row=3, column=2, sticky='e')
#
calculate = Button(text='Calculate', font=16, width=8,
                   command=lambda: messagebox.showinfo('Result', operator.get_result()) if operator else
                   messagebox.showerror('Error', 'Sets-operands are not correct'))
calculate.grid(row=7, column=2, sticky='w')
read_from_csv_but = Button(text='Read data from csv file', font=16, width=20, command=read_from_csv)
read_from_csv_but.grid(row=7, column=1, sticky='w')
#
#
win_2 = MyWindow()
win_2_menu = NavMenu()
win_2.win.config(menu=win_2_menu.menu)
# sets output, text frame for output
sets_frame_buts_w4 = Frame(win_2.win)
show_A = Button(sets_frame_buts_w4, height=2, text="Show A", command=show_a_callback)
show_B = Button(sets_frame_buts_w4, height=2, text="Show B", command=show_b_callback)
show_C = Button(sets_frame_buts_w4, height=2, text="Show C", command=show_c_callback)
show_A.grid(row=1, column=1, sticky="w")
show_B.grid(row=1, column=2, sticky="w")
show_C.grid(row=1, column=3, sticky="w")
text_field = Text(sets_frame_buts_w4, width=60, height=9, font="Arial 14")
text_field.grid(row=2, column=1, columnspan=3, sticky="w")
sets_frame_buts_w4.grid(row=1, column=1, sticky="w")
# step by step calculations
steps = Frame(win_2.win)
step_1 = Button(steps, text="Step 1", font=16, command=step_1_callback)
step_2 = Button(steps, text="Step 2", font=16, command=step_2_callback)
step_3 = Button(steps, text="Step 3", font=16, command=step_3_callback)
step_4 = Button(steps, text="Step 4", font=16, command=step_4_callback)
step_5 = Button(steps, text="Step 5", font=16, command=step_5_callback)
step_6 = Button(steps, text="Step 6", font=16, command=step_6_callback)
step_7 = Button(steps, text="Step 7", font=16, command=step_7_callback)
step_1.grid(row=1, column=1, sticky='w')
step_2.grid(row=1, column=2, sticky='w')
step_3.grid(row=1, column=3, sticky='w')
step_4.grid(row=1, column=4, sticky='w')
step_5.grid(row=1, column=5, sticky='w')
step_6.grid(row=1, column=6, sticky='w')
step_7.grid(row=1, column=7, sticky='w')
save = Button(steps, height=1, text="save this step", font=16,
              command=lambda: print(text_field.get('1.0', 'end-1c'), file=filedialog.asksaveasfile(parent=win_2.win)))
save.grid(row=1, column=8)
steps.grid(row=2, column=1, sticky="w")
win_2.win.withdraw()
#
win_3 = MyWindow()
win_3_menu = NavMenu()
win_3.win.config(menu=win_3_menu.menu)
sets_frame_buts_n = Frame(win_3.win)
show_A_n = Button(sets_frame_buts_n, height=2, text="Show A", command=show_a_w3_callback)
show_B_n = Button(sets_frame_buts_n, height=2, text="Show B", command=show_b_w3_callback)
show_C_n = Button(sets_frame_buts_n, height=2, text="Show C", command=show_c_w3_callback)
show_A_n.grid(row=1, column=1, sticky="w")
show_B_n.grid(row=1, column=2, sticky="w")
show_C_n.grid(row=1, column=3, sticky="w")
text_field_n = Text(sets_frame_buts_n, width=60, height=9, font="Arial 14")
text_field_n.grid(row=2, column=1, columnspan=3, sticky="w")
sets_frame_buts_n.grid(row=1, column=1, columnspan=3, sticky="w")
#
steps_s = Frame(win_3.win)
step_1 = Button(steps_s, text="Step 1", font=16, command=step_1_s_callback)
step_2 = Button(steps_s, text="Step 2", font=16, command=step_2_s_callback)
step_1.grid(row=1, column=1, sticky='w')
step_2.grid(row=1, column=2, sticky='w')
save = Button(steps_s, height=1, text="save this step", font=16,
              command=lambda: print(text_field_n.get('1.0', 'end-1c'), file=filedialog.asksaveasfile(parent=win_2.win)))
save.grid(row=1, column=3, sticky='w')
steps_s.grid(row=2, column=1, sticky='w')
win_3.win.withdraw()
#

win_4 = MyWindow()
win_4_menu = NavMenu()
win_4.win.config(menu=win_4_menu.menu)
sets_frame_buts_w4 = Frame(win_4.win)
show_X = Button(sets_frame_buts_w4, height=2, text="Show X", command=show_x_callback)
show_Y = Button(sets_frame_buts_w4, height=2, text="Show Y", command=show_y_callback)
calculate_Z = Button(sets_frame_buts_w4, height=2, text="Calculate Z", command=calculate_z_callback)
show_X.grid(row=1, column=1, sticky="w")
show_Y.grid(row=1, column=2, sticky="w")
calculate_Z.grid(row=1, column=3, sticky='w')
text_field_4 = Text(sets_frame_buts_w4, width=60, height=9, font="Arial 14")
text_field_4.grid(row=2, column=1, columnspan=3, sticky="w")
sets_frame_buts_w4.grid(row=1, column=1, sticky="w")
win_4.win.withdraw()
run_unittest = Button(win_4.win, text='Run Unit tests', command=run_unittest_callback)
run_unittest.grid(row=3, column=1, sticky='w')
#
win_5 = MyWindow()
win_5_menu = NavMenu()
win_5.win.config(menu=win_5_menu.menu)
win_5.win.withdraw()


root.mainloop()
