import unittest
import lists


def format_message(xs, expected, actual):
    return 'input: {}, expected: {}, actual: {}'.format(
        xs,
        expected,
        actual
    )


class TestMax(unittest.TestCase):
    test_cases = [
        {'input': [1, 2, 3],
         'min': 1,
         'max': 3,
         'sum': 6,
         'median': 2,
         'average': 2},
        {'input': [3, 2, 1],
         'min': 1,
         'max': 3,
         'sum': 6,
         'median': 2,
         'average': 2},
        {'input': [1, 3, 2],
         'min': 1,
         'max': 3,
         'sum': 6,
         'median': 2,
         'average': 2},
        {'input': [1, 4, 3, 2],
         'min': 1,
         'max': 4,
         'sum': 10,
         'median': 2.5,
         'average': 2.5}
    ]

    def test_max(self):
        for tt in self.test_cases:
            xs = tt['input']

            max_x = tt['max']
            actual_max_x = lists.max(xs)
            self.assertEqual(
                actual_max_x,
                max_x,
                format_message(xs, max_x, actual_max_x)
            )

            min_x = tt['min']
            actual_min_x = lists.min(xs)
            self.assertEqual(
                actual_min_x,
                min_x,
                format_message(xs, min_x, actual_min_x))

            expected_sum = tt['sum']
            actual_sum = lists.sum(xs)
            self.assertEqual(
                actual_sum,
                expected_sum,
                format_message(xs, expected_sum, actual_sum))

            expected_median = tt['median']
            actual_median = lists.median(xs)
            self.assertEqual(
                actual_median,
                expected_median,
                format_message(xs, expected_median, actual_median))

            expected_average = tt['average']
            actual_average = lists.average(xs)
            self.assertEqual(
                actual_average,
                expected_average,
                format_message(xs, expected_average, actual_average))


if __name__ == '__main__':
    unittest.main()
