import unittest
import find_pairs_equal_to_sum

def fun(x):
    return x + 1

class TestPair(unittest.TestCase):
    def testBruteForcePositiveNumbers(self):
        default_arr = [2, 6, 3, 9, 11]
        sum = 9
        pairs  =  find_pairs_equal_to_sum.brute_force(default_arr, sum)
        self.assertEqual(len(pairs), 1)

    def testBruteWithNegative(self):
        default_arr = [2, 6, 3, -9, 11]
        sum = 9
        pairs  =  find_pairs_equal_to_sum.brute_force(default_arr, sum)
        self.assertEqual(len(pairs), 1)

    def testOnePassSol(self):
        default_arr = [2, 6, 3, 9, 11]
        sum = 9
        pairs  =  find_pairs_equal_to_sum.one_pass_sol(default_arr, sum)
        self.assertEqual(len(pairs), 1)

    def testOnePassSolWithNeg(self):
        default_arr = [2, 6, 3, -9, 11]
        sum = 9
        pairs  =  find_pairs_equal_to_sum.one_pass_sol(default_arr, sum)
        self.assertEqual(len(pairs), 1)

    def testInPlaceWithSort(self):
        default_arr = [2, 6, 3, 9, 11]
        sum = 9
        pairs  =  find_pairs_equal_to_sum.in_place_with_sort(default_arr, sum)
        self.assertEqual(len(pairs), 1)

if __name__ == '__main__':
    unittest.main()
