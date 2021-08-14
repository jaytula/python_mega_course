from typing import List
import unittest


def mean(numbers: List[int]) -> float:
    return sum(numbers)/len(numbers)


def just_pass():
    pass


class FunctionsAndConditionals(unittest.TestCase):
    def test_creating_functions(self):
        self.assertAlmostEqual(mean([3, 4, 5, 6]), 4.5)

    def test_function_that_has_no_reutrn(self):
        self.assertEqual(just_pass(), None)


if __name__ == '__main__':
    unittest.main()