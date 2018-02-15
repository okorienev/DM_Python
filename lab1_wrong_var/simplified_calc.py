class SimplifiedCalculation:
    def __init__(self, a_set, b_set, c_set, universal_set):
        self.A = a_set
        self.B = b_set
        self.C = c_set
        self.universal_set = universal_set
        self.result_D = set()
        self.res_1_d = set()

    def step1(self):
        if not self.res_1_d:
            self.res_1_d = self.A.intersection(self.universal_set - self.C)
            return self.res_1_d
        else:
            return self.res_1_d

    def step_2(self):
        if not self.result_D:
            if not self.res_1_d:
                self.step1()
                self.result_D = self.B.intersection(self.res_1_d)
                return self.result_D
            else:
                self.result_D = self.B.intersection(self.res_1_d)
                return self.result_D
        else:
            return self.result_D



