# -*- coding: utf-8 -*-


import unittest
from unittest.mock import Mock

from lesson_014.bowling import get_score

_test_data1 = '-/37X1/3415XX629-'
_test_data2 = 'X1/253/X5572811/X'


class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        fake_result = Mock()
        fake_result.text = _test_data1
        result = get_score(fake_result.text)
        self.assertEqual(130, result)

    def test_normal_2(self):
        fake_result = Mock()
        fake_result.text = _test_data2
        result = get_score(fake_result.text)
        self.assertEqual(result, 140)


if __name__ == '__main__':
    unittest.main()