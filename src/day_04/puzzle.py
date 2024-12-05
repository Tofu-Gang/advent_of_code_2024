__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from typing import Tuple
from .word_puzzle import WordPuzzle


################################################################################

def _is_x_mas(row: int, column: int, lines: Tuple[str, ...]) -> bool:
    """

    :param row:
    :param column:
    :param lines:
    :return:
    """

    leg_1 = (lines[row][column] +
             lines[row + 1][column + 1] +
             lines[row + 2][column + 2])
    leg_2 = (lines[row][column + 2] +
             lines[row + 1][column + 1] +
             lines[row + 2][column])

    return (leg_1 == "MAS" or leg_1 == "SAM") and (leg_2 == "MAS" or leg_2 == "SAM")


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    return WordPuzzle().word_search


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    with open("src/day_04/input.txt", "r") as f:
        lines = tuple(f.readlines())
        count = 0
        for row in range(len(lines) - 2):
            for column in range(len(lines[row]) - 2):
                if _is_x_mas(row, column, lines):
                    count += 1
        return count

################################################################################
