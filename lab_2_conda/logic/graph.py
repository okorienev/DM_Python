import networkx as nx
from logic.relations import RelationMaker
import matplotlib.pyplot as plt

# TODO clear test stuff
# TODO draw edges with different colors
# A_set = {choice(list(chain(female_objects, male_objects))) for i in range(10)}
# B_set = {choice(list(chain(female_objects, male_objects))) for i in range(10)}


class GraphDrawer:
    def __init__(self, set_a, set_b):
        self.relation_maker = RelationMaker(set_a, set_b)
        self.relation_maker.delete_impossible_mother_relation()
        self.relation_maker.delete_impossible_for_mother_in_law_relation()
        self.relation_maker.form_mother_child_relation()
        self.relation_maker.form_mother_in_law_relation()
        self.graph_mother = nx.DiGraph()
        self.graph_mother_in_law = nx.DiGraph()
        # print(self.relation_maker.set_a, self.relation_maker.set_b)
        # print()
        # print(self.relation_maker.set_a_operand_for_s, self.relation_maker.set_b_operand_for_s)
        # print()
        # print(self.relation_maker.set_a_operand_for_r, self.relation_maker.set_b_operand_for_r)
        # print(self.relation_maker.s_relation)
        # print(self.relation_maker.r_relation)

    @staticmethod
    def _clear_plot():
        plt.clf()
        plt.cla()
        plt.close()

    def draw_graph_mother(self):
        self._clear_plot()
        # self.add_nodes()
        # self.add_edges_mother()
        for i in self.graph_mother.nodes.items():
            pass

    def draw_graph_mother_in_law(self):
        self._clear_plot()
        # self.add_nodes()
        # self.add_edges_mother_in_law()
        pos = nx.spring_layout(self.graph_mother_in_law)
        nx.draw_networkx_nodes(self.graph_mother_in_law,
                               pos=pos,
                               nodelist=[i.name for i in self.relation_maker.set_b],
                               node_color='yellow')
        nx.draw_networkx_nodes(self.graph_mother_in_law,
                               pos=pos,
                               nodelist=[i.name for i in self.relation_maker.set_a],
                               node_color='b')
        nx.draw_networkx_labels(self.graph_mother_in_law,
                                pos=pos,
                                labels=dict(zip([i.name for i in self.relation_maker.set_a],
                                                [i.name for i in self.relation_maker.set_a])),
                                font_color='black')
        nx.draw_networkx_labels(self.graph_mother_in_law,
                                pos=pos,
                                labels=dict(zip([i.name for i in self.relation_maker.set_b],
                                                [i.name for i in self.relation_maker.set_b])),
                                font_color='black')
        nx.draw_networkx_edges(self.graph_mother_in_law,
                               pos=pos,
                               edgelist=self.relation_maker.r_relation,
                               edge_color='red')
        print(self.relation_maker.r_relation)
        plt.show()


# graph = GraphDrawer(A_set, B_set)
# graph.draw_graph_mother_in_law()
# graph.draw_graph_mother()
