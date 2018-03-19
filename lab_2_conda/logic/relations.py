from itertools import cycle
# TODO clear all test stuff


class RelationMaker:
    """making relations with given variant
    aSb if a is mother of b
    aRb if a is mother-in-law of b
    """

    def __init__(self, set_a, set_b):
        self.set_a = set_a
        self.set_b = set_b
        self.set_a_operand_for_s = self.set_a.copy()
        self.set_b_operand_for_s = self.set_b.copy()
        self.set_a_operand_for_r = self.set_a.copy()
        self.set_b_operand_for_r = self.set_b.copy()
        self.s_relation = set()
        self.r_relation = set()

    def delete_impossible_mother_relation(self):
        """male can't be mother or mother-in-law"""
        for i in self.set_a:
            if i.GENDER == 'male':
                self.set_a_operand_for_s.discard(i)

    def delete_impossible_for_mother_in_law_relation(self):
        """
        male can't be mother or mother-in-law
        task was given in ukrainian
        marrieds have different terms for parents in law so in this task female can't have mother in law
        """
        for i in self.set_a:
            if i.GENDER == 'male':
                self.set_a_operand_for_r.discard(i)
        for i in self.set_b:
            if i.GENDER == 'female':
                self.set_b_operand_for_r.discard(i)

    def form_mother_child_relation(self):
        for i in zip(cycle(self.set_a_operand_for_s), self.set_b_operand_for_s):
            if i[0].name != i[1].name:
                self.s_relation.add((i[0].name, i[1].name))

    def form_mother_in_law_relation(self):
        # DEPRECATED
        # iter_counter = len(self.set_b_operand_for_r)**2
        # need_counter = len(self.set_b_operand_for_r)
        # while iter_counter > 0 and need_counter > 0:
        #     for i in zip(cycle(self.set_a_operand_for_r), self.set_b_operand_for_r):
        #         print(*i)
        #         if (i[0].name, i[1].name) not in self.s_relation:
        #             self.r_relation.add((i[0].name, i[1].name))
        #             need_counter -= 1
        #         iter_counter -= 1
        #     self.set_b_operand_for_r = set(list(self.set_b_operand_for_r))
        #     self.set_a_operand_for_r = set(list(self.set_a_operand_for_r))
        for i in self.set_b_operand_for_r:
            for j in set(list(self.set_a_operand_for_r)):
                if (j.name, i.name) not in self.s_relation:
                    self.r_relation.add((j.name, i.name))
                    break


# relation_maker = RelationMaker(A, B)
# print(relation_maker.set_a, '\n', relation_maker.set_b)
# relation_maker.delete_impossible_mother_relation()
# print(relation_maker.set_a_operand_for_s, '\n', relation_maker.set_b_operand_for_s)
# relation_maker.delete_impossible_for_mother_in_law_relation()
# print(relation_maker.set_a_operand_for_r, '\n', relation_maker.set_b_operand_for_r)
