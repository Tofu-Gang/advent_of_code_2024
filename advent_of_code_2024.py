__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
The Chief Historian is always present for the big Christmas sleigh launch, but 
nobody has seen him in months! Last anyone heard, he was visiting locations that 
are historically significant to the North Pole; a group of Senior Historians has 
asked you to accompany them as they check the places they think he was most 
likely to visit.

As each location is checked, they will mark it on their list with a star. They 
figure the Chief Historian must be in one of the first fifty places they'll 
look, so in order to save Christmas, you need to help them get fifty stars on 
their list before Santa takes off on December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day 
in the Advent calendar; the second puzzle is unlocked when you complete the 
first. Each puzzle grants one star. Good luck!
"""

from unittest import TestCase, main

from src.day_01 import puzzle as day_01
from src.day_02 import puzzle as day_02
from src.day_03 import puzzle as day_03
from src.day_04 import puzzle as day_04
from src.day_05 import puzzle as day_05
from src.day_10 import puzzle as day_10


################################################################################

class TestAdventOfCode2024(TestCase):

    def test_advent_of_code_2024(self):
        self.assertEqual(day_01.puzzle_01(), 2756096)
        self.assertEqual(day_01.puzzle_02(), 23117829)
        self.assertEqual(day_02.puzzle_01(), 359)
        self.assertEqual(day_02.puzzle_02(), 418)
        self.assertEqual(day_03.puzzle_01(), 162813399)
        self.assertEqual(day_03.puzzle_02(), 53783319)
        self.assertEqual(day_04.puzzle_01(), 2447)
        self.assertEqual(day_04.puzzle_02(), 1868)
        self.assertEqual(day_05.puzzle_01(), 4905)
        self.assertEqual(day_05.puzzle_02(), 6204)
        self.assertEqual(day_10.puzzle_01(), -1)
        self.assertEqual(day_10.puzzle_02(), -1)

################################################################################


if __name__ == '__main__':
    main()

################################################################################
