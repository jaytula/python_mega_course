from typing import List, Dict, Union
import unittest


def mean(value: Union[List[int], Dict[str, float]]) -> int:
    if isinstance(value, list):
        return sum(value) // len(value)
    
    dict_values = value.values()
    return int(sum(dict_values) // len(dict_values))


def just_pass():
    pass


class FunctionsAndConditionals(unittest.TestCase):
    def test_creating_functions(self):
        self.assertAlmostEqual(mean([3, 4, 5, 6]), 4)
        student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
        self.assertAlmostEqual(mean(student_grades), 8, 2)

    def test_function_that_has_no_return(self):
        self.assertEqual(just_pass(), None)


if __name__ == '__main__':
    unittest.main()