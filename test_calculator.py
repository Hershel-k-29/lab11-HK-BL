import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    pass
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(6, 7), 13)
        self.assertNotEqual(add(6, 7), 69)
        self.assertEqual(add(1, -10), -9)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(76, 6), 70)
        self.assertNotEqual(sub(6, 7), 69)
        self.assertEqual(sub(10, -10), 20)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(5, -1), -5)
        self.assertEqual(mul(0, 1), 0)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-1, 10), -10)
        self.assertRaises(ZeroDivisionError, div, 0, 5)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(555, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0 ,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()