class FullCalculation:
    """methods make step by step calculations of given expression
result of each step can be obtained by initializing object
with appropriate sets and calling method of needed step
    """

    def __init__(self, a_set, b_set, c_set, universal_set):
        self.A = a_set
        self.B = b_set
        self.C = c_set
        self.universal_set = universal_set
        self.result_D = set()
        self.res_1_d = set()
        self.res_2_d = set()
        self.res_3_d = set()
        self.res_4_d = set()
        self.D_impossible_to_calculate_flag = False

    def step_1_d(self):
        try:
            if not self.res_1_d:
                self.res_1_d = self.A.intersection(self.B)
                return self.res_1_d
            else:
                return self.res_1_d
        except TypeError:
            self.D_impossible_to_calculate_flag = True

    def step_2_d(self):
        try:
            if not self.res_2_d:
                self.res_2_d = self.A.intersection(self.universal_set - self.C)
                return self.res_2_d
            else:
                return self.res_2_d
        except TypeError:
            self.D_impossible_to_calculate_flag = True

    def step_3_d(self):
        try:
            if not self.res_3_d:
                self.res_3_d = (self.universal_set - self.A).intersection(self.B)
                return self.res_3_d
            else:
                return self.res_3_d
        except TypeError:
            self.D_impossible_to_calculate_flag = True

    def step_4_d(self):
        try:
            if not self.res_4_d:
                if not self.res_3_d or not self.res_2_d:
                    self.step_3_d()
                    self.step_2_d()
                self.res_4_d = self.res_3_d.union(self.res_2_d)
                return self.res_4_d
            else:
                return self.res_4_d
        except TypeError:
            self.D_impossible_to_calculate_flag = True

    def step_5_d_final(self):
        try:
            if not self.result_D:
                if not self.res_4_d or not self.res_1_d:
                    self.step_1_d()
                    self.step_4_d()
                self.result_D = self.res_1_d.union(self.res_4_d)
                return self.result_D
            else:
                return self.result_D
        except TypeError:
            self.D_impossible_to_calculate_flag = True
