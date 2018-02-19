class MySet:
    def __init__(self, iterable):
        self.set = set()
        for i in iterable:
            self.set.add(i)

    def addiction(self, universal):
        return {i for i in universal if i not in self.set}

    def union(self, operand_2):
        res = set()
        for i in self.set:
            res.add(i)
        for i in operand_2:
            if i not in res:
                res.add(i)
        return res


if __name__ == '__main__':
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    c = MySet(a)
    print(c.set)
    print(c.union(b))