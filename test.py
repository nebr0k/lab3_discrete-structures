import unittest

from main import permutation_count


class TestPermutationCount(unittest.TestCase):
    def test_permutation_count(self):
        self.assertEqual(permutation_count(8, 8), 40320)
        self.assertEqual(permutation_count(5, 2), 20)
        self.assertEqual(permutation_count(10, 5), 30240)

if __name__ == '__main__':
    unittest.main()
