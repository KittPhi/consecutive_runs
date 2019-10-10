import unittest
from consecutive_runs import find_consecutive_runs


class TestConsecutiveRuns(unittest.TestCase):

    def test_empty_input(self):
        _input_numbers = []
        self.assertEqual(find_consecutive_runs(_input_numbers), None)

    def test_less_than_three_numbers(self):
        _input_numbers = [0, 1]
        self.assertEqual(find_consecutive_runs(_input_numbers), None)

    def test_three_increasing_consecutive_numbers(self):
        _input_numbers = [0, 1, 2]
        self.assertEqual(find_consecutive_runs(_input_numbers), [0])

    def test_three_decreasing_consecutive_numbers(self):
        _input_numbers = [2, 1, 0]
        self.assertEqual(find_consecutive_runs(_input_numbers), [0])

    def test_three_non_consecutive_numbers(self):
        _input_numbers = [0, 1, 3]
        self.assertEqual(find_consecutive_runs(_input_numbers), None)

    def test_equal_numbers(self):
        _input_numbers = [1, 1, 1]
        self.assertEqual(find_consecutive_runs(_input_numbers), None)

    def test_large_list(self):
        """
        This can be tested for much larger numbers too but would the algorithm needs be modified to be scalable.
        One way to scale would be to use an algorithm similar to merge sort or chunks and queues.
        """
        _count = 100000
        _input_numbers = list(range(_count))
        self.assertEqual(find_consecutive_runs(_input_numbers), list(range(_count - 2)))

    def test_sample_from_requirements(self):
        """
        Test case given in requirements.
        """
        _input_numbers = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
        self.assertEqual(find_consecutive_runs(_input_numbers), [0, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
