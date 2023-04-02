import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    # 每一個testcase開始前都會被呼叫 -> 前置作業
    def setUp(self):
        self.cal = Calculator(3, 0)

    # 每一個testcase結束後會被呼叫 -> 清理善後作業
    def tearDown(self):
        self.cal = None

    def test_plus(self):
        expected = 3
        result = self.cal.plus()
        self.assertEqual(expected, result)

    def test_minus(self):
        expected = 3
        result = self.cal.plus()
        self.assertEqual(expected, result)

    def test_multiple(self):
        expected = 0
        result = self.cal.multiple()
        self.assertEqual(expected, result)

    def test_mod_divided_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.cal.mod)


if __name__ == '__main__':
    unittest.main()
