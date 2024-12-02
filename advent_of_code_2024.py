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


################################################################################

class TestAdventOfCode2024(TestCase):

    def test_advent_of_code_2024(self):
        self.assertEqual(day_01.puzzle_01(), 2756096)
        self.assertEqual(day_01.puzzle_02(), 23117829)
        self.assertEqual(day_02.puzzle_01(), 359)
        self.assertEqual(day_02.puzzle_02(), 418)

################################################################################


if __name__ == '__main__':
    main()

################################################################################
