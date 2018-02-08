class FullCalculation:
    def __init__(self, set_a, set_b, set_c, universal_set):
        self.result_1 = set()
        self.result_2 = set()
        self.result_3 = set()
        self.result_4 = set()
        self.result_5 = set()
        self.result_6 = set()
        self.result_final = set()
        self.A = set_a
        self.B = set_b
        self.C = set_c
        self.U = universal_set

    def step_1(self):
        if not self.result_1:
            self.result_1 = self.A.union(self.B)
            return self.result_1
        else:
            return self.result_1

    def step_2(self):
        if not self.result_2:
            self.result_2 = self.A.union(self.U - self.B)
            return self.result_2
        else:
            return self.result_2

    def step_3(self):
        if not self.result_3:
            self.result_3 = (self.U - self.A).union(self.C)
            return self.result_3
        else:
            return self.result_3

    def step_4(self):
        if not self.result_1 or not self.result_2:
            self.step_1()
            self.step_2()
        if not self.result_4:
            self.result_4 = self.result_1.union(self.result_2)
            return self.result_4
        else:
            return self.result_4

    def step_5(self):
        if not self.result_5:
            if not self.result_4:
                self.step_4()
            self.result_5 = self.result_4.intersection(self.U - self.B)
            return self.result_5
        else:
            return self.result_5

    def step_6(self):
        if not self.result_6:
            if not self.result_5:
                self.step_5()
            self.result_6 = self.result_5.intersection(self.A)
            return self.result_6
        else:
            return self.result_6

    def get_result(self):
        if not self.result_final:
            if not self.result_6 or not self.result_3:
                self.step_3()
                self.step_6()
            self.result_final = self.result_6.intersection(self.result_3)
            return self.result_final
        else:
            return self.result_final
