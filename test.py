import unittest
from app import fibonacci

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_normal(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_large_number(self):
        # 大きな数値に対するテスト
        self.assertEqual(fibonacci(50), 12586269025)

    def test_fibonacci_invalid_input(self):
        # 不正な入力に対するテスト
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(0)

    def test_fibonacci_non_integer_input(self):
        # 非整数値に対するテスト
        with self.assertRaises(ValueError):
            fibonacci("a")
        with self.assertRaises(ValueError):
            fibonacci(5.5)

if __name__ == '__main__':
    unittest.main()
