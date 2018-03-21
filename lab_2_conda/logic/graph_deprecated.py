# Deprecated stuff
# def add_nodes(self):
#     for i in self.relation_maker.set_a:
#         self.graph_mother.add_node(i.name, set='a')
#         self.graph_mother_in_law.add_node(i.name, set='a')
#     for i in self.relation_maker.set_b:
#         self.graph_mother.add_node(i.name, set='b')
#         self.graph_mother_in_law.add_node(i.name, set='b')
#
# def add_edges_mother(self):
#     for i in self.relation_maker.s_relation:
#         self.graph_mother.add_edge(i[0], i[1])
#
# def add_edges_mother_in_law(self):
#     for i in self.relation_maker.r_relation:
#         self.graph_mother_in_law.add_edge(i[0], i[1])
#
#     def draw_graph_mother(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother()
#         nx.draw(self.graph_mother, with_labels=True)
#         plt.show()
#
#     def draw_graph_mother_in_law(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother_in_law()
#         nx.draw(self.graph_mother_in_law, with_labels=True)
#         plt.show()
#
#     def draw_graphs_union(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother()
#         self.add_edges_mother_in_law()
#         graph_union = nx.union(self.graph_mother, self.graph_mother_in_law)
#         nx.draw(graph_union, with_labels=True)
#         plt.show()
#
#     def draw_graphs_intersection(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother()
#         self.add_edges_mother_in_law()
#         graph_intersection = nx.intersection(self.graph_mother_in_law, self.graph_mother)
#         nx.draw(graph_intersection, with_labels=True)
#         plt.show()
#
#     def draw_graph_symmetric_difference(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother()
#         self.add_edges_mother_in_law()
#         graph_symmetric_difference = nx.symmetric_difference(self.graph_mother_in_law, self.graph_mother)
#         nx.draw(graph_symmetric_difference, with_labels=True)
#         plt.show()
#
#     def draw_graph_u_symmetric_with_r(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother_in_law()
#         universal = nx.DiGraph()
#         for i in self.relation_maker.set_a:
#             universal.add_node(i.name, set='a')
#         for i in self.relation_maker.set_b:
#             universal.add_node(i.name, set='b')
#         for i in self.relation_maker.set_a:
#             for j in self.relation_maker.set_b:
#                 universal.add_edge(i.name, j.name)
#         nx.draw(nx.symmetric_difference(universal, self.graph_mother_in_law))
#         plt.show()
#
#     def draw_graph_reversed_s(self):
#         plt.clf()
#         plt.cla()
#         plt.close()
#         self.add_nodes()
#         self.add_edges_mother()
#         nx.draw(self.graph_mother.reverse())
#         plt.show()
# Deprecated end
