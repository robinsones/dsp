from __future__ import division
import unittest
<<<<<<< HEAD
from jaccard.py import j
=======
from scipy.spatial.distance import jaccard
>>>>>>> eac3ef55c7789b84377ce37284233a147996a594


class TestJ(unittest.TestCase):

    def test_fails_on_no_args(self):
        with self.assertRaises(TypeError):
            j()

    def test_fails_on_one_arg(self):
        with self.assertRaises(TypeError):
            j(1)

    def test_fails_on_three_args(self):
        with self.assertRaises(TypeError):
            j(1, 2, 3)

    def test_one_for_same(self):
        result = j([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, 1)

    def test_result_is_float(self):
        result = j([1, 2, 3], [1, 2, 3])
        self.assertIs(type(result), type(1.0))

    def test_order_not_important(self):
        result = j([3, 2, 1], [1, 3, 2])
        self.assertEqual(result, 1)

    def test_zero_for_different(self):
        result = j([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, 0)

    def test_half_for_double(self):
        result = j(['cow'], ['dog', 'cow'])
        self.assertEqual(result, 0.5)

    def test_third_for_half_same(self):
        result = j([1, 2], [2, 3])
        self.assertEqual(result, 1/3)

    def test_half_for_two_thirds_same(self):
        result = j([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, 0.5)

    def test_immune_to_duplicates(self):
        result = j([1, 1, 2], [3, 3, 3, 2, 2])
        self.assertEqual(result, 1/3)

    def test_larger_lists(self):
        result = j(range(1, 10), [10, 9, 8, 7, 6])
        self.assertEqual(result, 2/5)

if __name__ == '__main__':
    unittest.main()
