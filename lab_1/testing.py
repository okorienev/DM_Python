import full_calculation as fc
import simplified_calculation as sc
from task_2 import MySet
import unittest


data = {1: [{1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}, {5, 6, 7, 8, 9}, {i for i in range(11)}],
        2: [{2, -5, 5, -1}, {2, -3, -1}, {2, -4, -3, -1, -2}, {i for i in range(-5, 6)}],
        3: [{0, 3, 13, 14}, {9, 10, 14}, {10, 3, 4, 12, 7}, {i for i in range(16)}],
        4: [{16, 8, 10, 14, 7}, {5, 6, 10, 13, 17, 20}, {5, 6, 9, 15, 16, 17, 19}, {i for i in range(5, 21)}],
        5: [{2, 4, 6, 8, 10, 12, 14, 16, 18}, {3}, {3, 5, 7, 9, 11, 13, 15}, {i for i in range(5, 21)}],
        6: [{-5, -4, -3, -2, -1}, {1, 2, 3}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {i for i in range(-5, 11)}],
        7: [{0}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {-1, -2, -3, -4, -5, -6, -7, -8, -9}, {i for i in range(-9, 11)}],
        8: [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 7}, {1, 2, 3, 4, 5, 6}, {i for i in range(1, 10)}],
        9: [{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {i for i in range(1, 6)}],
        10: [{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {i for i in range(1, 7)}]}


class TestCalculationEquality(unittest.TestCase):
    def test_case1(self):
        operator1 = fc.FullCalculation(*data.get(1))
        operator2 = sc.SimplifiedCalculation(*data.get(1))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case2(self):
        operator1 = fc.FullCalculation(*data.get(2))
        operator2 = sc.SimplifiedCalculation(*data.get(2))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case3(self):
        operator1 = fc.FullCalculation(*data.get(3))
        operator2 = sc.SimplifiedCalculation(*data.get(3))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case4(self):
        operator1 = fc.FullCalculation(*data.get(4))
        operator2 = sc.SimplifiedCalculation(*data.get(4))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case5(self):
        operator1 = fc.FullCalculation(*data.get(5))
        operator2 = sc.SimplifiedCalculation(*data.get(5))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case6(self):
        operator1 = fc.FullCalculation(*data.get(6))
        operator2 = sc.SimplifiedCalculation(*data.get(6))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case7(self):
        operator1 = fc.FullCalculation(*data.get(7))
        operator2 = sc.SimplifiedCalculation(*data.get(7))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case8(self):
        operator1 = fc.FullCalculation(*data.get(8))
        operator2 = sc.SimplifiedCalculation(*data.get(8))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case9(self):
        operator1 = fc.FullCalculation(*data.get(9))
        operator2 = sc.SimplifiedCalculation(*data.get(9))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case10(self):
        operator1 = fc.FullCalculation(*data.get(10))
        operator2 = sc.SimplifiedCalculation(*data.get(10))
        self.assertEqual(operator1.get_result(), operator2.get_result())

    def test_case_union_MySet(self):
        for i in data.values():
            operand = MySet(i[0])
            self.assertEqual(i[0].union(i[1]), operand.union(i[1]))

    def test_case_addiction_MySet(self):
        for i in data.values():
            operand = MySet(i[0])
            self.assertEqual(i[3] - (i[0]), operand.addiction(i[3]))


if __name__ == '__main__':
    unittest.main()
