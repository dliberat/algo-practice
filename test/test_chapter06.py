import unittest

import algo as algo


class TestAlgos(unittest.TestCase):

    def test_6_1(self):
        tests = [
            ([], []),
            ([1,1,1,1], [1,1,1,1]),
            ([1,1,1,1,], [1,1,1,1,-3]),
            ([4], [2,1,-3,4]),
            ([2, 2], [2,1,-3,2,2]),
            ([10,-5,40,10], [5,15,-30,10,-5,40,10])
        ]
        for expected_output, array in tests:
            actual_output = algo.contiguous_sum_6_1(array)
            self.assertListEqual(expected_output, actual_output)
    
    def test_6_2(self):
        tests = [
            ([200, 400, 600, 800, 1000], [200, 400, 600, 800, 1000]),
            ([100, 200, 400, 500, 600, 800], [200, 400, 600, 800]),
            ([10, 20, 30, 40, 50], [50]),
            ([150, 300, 500, 700], [150, 300, 500, 700]),
            ([200, 400, 600, 900], [200, 400, 600, 900]),
            ([200, 390, 400, 580, 600, 700, 900], [200, 390, 580, 700, 900]),
        ]
        for array, expected_output in tests:
            actual_output = algo.hotel_stops_6_2(array)
            self.assertListEqual(expected_output, actual_output)

    def test_6_4(self):
        wordset = set(['a', 'at', 'apple', 'be', 'bat', 'banana', 'cat',
            'car', 'card', 'carpet'])
        is_word = lambda x: x in wordset

        valid_texts = [
            ['a', 'cat', 'be', 'carpet'],
            ['bat', 'cat', 'car', 'apple'],
        ]
        invalid_texts = [
            ['invalid', 'text'],
            ['be', 'banana', 'cat', 'o', 'card'],
        ]

        for arr in valid_texts:
            text = ''.join(arr)
            res, words = algo.word_split_6_4(text, is_word)
            self.assertTrue(res, msg=f'"{text}" is a valid string of words')
            self.assertListEqual(arr, words)

        for arr in invalid_texts:
            text = ''.join(arr)
            res, words = algo.word_split_6_4(text, is_word)
            self.assertFalse(res, msg=f'"{text}" is not a valid string of words')

    def test_6_5(self):
        inputset = [
            {
              'checkerboard': [
                    [ 1, -1,   1],
                    [ 1, -1,   1],
                    [ 5,  1,   1],
                    [-1,  1, 100],
                ],
              'best_score': 102,
            }
        ]

        for input in inputset:
            checkerboard = input['checkerboard']
            expected_best_score = input['best_score']

            best_score, best_pattern = algo.pebbling_a_checkerboard_6_5(checkerboard)
            self.assertEqual(expected_best_score, best_score)

    def test_6_6(self):
        inputset = [
            ('bbbbac', True),
            ('b', False),
            ('', False),
            ('aa', False),
            ('ab', False),
            ('ac', True),
            ('cac', True),
            ('cbc', True),
            ('caaccababb', True),
            ('ccccc', False),
            ('bbbbbb', False),
            ('cbbbb', False),
        ]
        for input, expected in inputset:
            msg = f'"{input}" should be {expected}'
            result = algo.symbol_multiplication_6_6(input)
            self.assertEqual(expected, result, msg=msg)
