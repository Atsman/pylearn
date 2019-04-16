import unittest
from primitives.specific_bit import specific_bit


class TestSpecificBit(unittest.TestCase):
    def test_specific_bit(self):
        test_cases = [
                    {
                        'input': [0b1111, 0, 0],
                        'output': 0b1110
                    },
                    {
                        'input': [0b1111, 1, 0],
                        'output': 0b1101
                    },
                    {
                        'input': [0b1111, 2, 0],
                        'output': 0b1011
                    },
                    {
                        'input': [0b1111, 3, 0],
                        'output': 0b111
                    },
                    {
                        'input': [0b0000, 0, 1],
                        'output': 0b1
                    },
                    {
                        'input': [0b0000, 1, 1],
                        'output': 0b10
                    },
                    {
                        'input': [0b0000, 2, 1],
                        'output': 0b100
                    },
                    {
                        'input': [0b0000, 3, 1],
                        'output': 0b1000
                    }
                ]

        for test_case in test_cases:
            self.assertEqual(test_case['output'],
                             specific_bit(*test_case['input']))


if __name__ == '__main__':
    unittest.main()
