import tkinter as tk
from lab_4.graph import GraphPainter


def collect_edges():
    print([tuple(i.replace('(', '').replace(')', '').split(',')) for i in text.get(1.0, tk.END).split()])
    global graph
    graph = GraphPainter(None,
                         [tuple(i.replace('(', '').replace(')', '').split(',')) for i in text.get(1.0, tk.END).split()])


root = tk.Tk()
graph = GraphPainter(
    [i for i in range(1, 11)],
    [(1, 3), (1, 6), (1, 7),
     (2, 8), (2, 7), (2, 8),
     (3, 9), (3, 4),
     (4, 5), (4, 9),
     (6, 7), (7, 8), (8, 9), (9, 10)]
)
f1 = tk.Frame()
button1 = tk.Button(f1, text="show raw graph", width=16, font=22, command=lambda: graph.draw_raw_graph())
button1.grid(row=1, column=1, sticky='n')
button2 = tk.Button(f1, text="show coloured graph", width=16, font=22, command=lambda: graph.draw_coloured_graph())
button2.grid(row=2, column=1, sticky='n')
button3 = tk.Button(f1, text="collect edges", width=16, font=22, command=collect_edges)
button3.grid(row=3, column=1, sticky='n')
text = tk.Text(height=20, width=30)
f1.grid(row=1, column=1, sticky='n')
text.grid(row=1, column=2, rowspan=1, sticky='w')
root.mainloop()
