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
        self.gaming_bowling.get_score('XXXXXXXXXX')
        self.assertEqual(self.gaming_bowling.total_score, 200)

    def test_spare(self):
        self.gaming_bowling.get_score('4/4/4/4/4/4/4/4/4/4/')
        self.assertEqual(self.gaming_bowling.total_score, 150)

    def test_count(self):
        self.gaming_bowling.get_score('45454545454545454545')
        self.assertEqual(self.gaming_bowling.total_score, 90)

    def test_raise_second_shot_strike(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('Xa/XXXXXXXXX')

    def test_raise_less_than_10_frames(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('XXXXXXXX')

    def test_raise_greater_equally_10_points(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_score('XXXXXXXXX82')


if __name__ == '__main__':
    unittest.main()
