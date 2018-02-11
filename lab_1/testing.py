import full_calculation as fc
import simplified_calculation as sc
import unittest


data = {1: [{1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}, {5, 6, 7, 8, 9}, {i for i in range(11)}],
        2: [{2, -5, 5, -1}, {2, -3, -1}, {2, -4, -3, -1, -2}, {i for i in range(-5, 6)}],
        3: [{0, 3, 13, 14}, {9, 10, 14}, {10, 3, 4, 12, 7}, {i for i in range(16)}],
        4: [{16, 8, 10, 14, 7}, {5, 6, 10, 13, 17, 20}, {5, 6, 9, 15, 16, 17, 19}, {i for i in range(5, 21)}]}


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


if __name__ == '__main__':
    unittest.main()
