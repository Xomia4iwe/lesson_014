# -*- coding: utf-8 -*-

import unittest
from bowling import Bowling


class MyBowlingTest(unittest.TestCase):

    def setUp(self):
        self.gaming_bowling = Bowling()

    def test_normal(self):
        self.gaming_bowling.get_score('X71-9X7/45-3-65/X')
        self.assertEqual(self.gaming_bowling.total_score, 125)

    def test_strike(self):
        self.gaming_bowling.get_score('X')
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('X7XXXXXXXX')

    def test_raise_null_in_game_result(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('XXXXXXX00XX')

        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('XXXXXXXXXXX')

    def test_raise_first_shot_spare(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('XXXXX/6XXXX')

    def test_raise_incorrect_char(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('Xa/XXXXXXXXX')


if __name__ == '__main__':
    unittest.main()
