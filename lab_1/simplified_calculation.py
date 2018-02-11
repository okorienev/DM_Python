class SimplifiedCalculation:
    def __init__(self, a, b, c, u):
        self.a = a
        self.b = b
        self.c = c
        self.u = u
        self.step_1_res = set()
        self.result = set()

    def step_1(self):
        if not self.step_1_res:
            self.step_1_res = (self.u - self.b).intersection(self.a)
            return self.step_1_res
        else:
            return self.step_1_res

    def get_result(self):
        if not self.step_1_res:
            self.step_1()
        if not self.result:
            self.result = self.step_1_res.intersection(self.c)
            return self.result
        else:
            return self.result


