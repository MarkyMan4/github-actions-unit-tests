import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_fibonacci(self):
        seq = [fib(i) for i in range(10)]
        correct_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        self.assertListEqual(seq, correct_seq)

    def test_get_index(self):
        xs = [1,2,3,4,5]

        ind1 = get_index(xs, 3)
        ind2 = get_index(xs, 6)

        self.assertEqual(ind1, 2)
        self.assertEqual(ind2, -1)

    def test_reverse_string(self):
        s = 'abcde'
        rev = reverse_string(s)

        self.assertEqual(rev, 'edcba')

if __name__ == '__main__':
    unittest.main()
