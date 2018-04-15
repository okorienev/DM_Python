import networkx as nx
import matplotlib.pyplot as plt


class GraphPainter:
    colours = [
        "blue",
        "red",
        "green",
        "yellow",
        "black",
        "pink",
        "brown"
    ]

    @staticmethod
    def _clear_plot():
        plt.clf()
        plt.cla()
        plt.close()

    def __init__(self, node_list=None, edge_list=None):
        if edge_list is None:
            edge_list = []
        if node_list is None:
            node_list = []
        self.graph = nx.Graph()
        for i in node_list:
            self.graph.add_node(i)
        for i in edge_list:
            self.graph.add_edge(*i)
        self.pos = nx.circular_layout(self.graph)

    def draw_raw_graph(self):
        self._clear_plot()
        nx.draw_networkx(self.graph, pos=self.pos, with_labels=True)
        plt.show()

    def draw_coloured_graph(self):
        self._clear_plot()
        colours = list(nx.greedy_color(self.graph).items())
        nx.draw_networkx_nodes(self.graph, pos=self.pos, nodelist=[i[0] for i in colours],
                               node_color=[i[1] for i in colours])
        nx.draw_networkx_edges(self.graph, self.pos)
        nx.draw_networkx_labels(self.graph, self.pos, font_color='violet')
        plt.show()
