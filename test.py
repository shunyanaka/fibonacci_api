import unittest
from app import fibonacci

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(ValueError):
            fibonacci(-1)
            fibonacci(0)

if __name__ == '__main__':
    unittest.main()
