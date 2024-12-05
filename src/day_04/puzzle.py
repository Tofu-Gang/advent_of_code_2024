__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple
from re import compile

"""

"""

INPUT_FILE_PATH = "src/day_04/input.txt"
XMAS = "XMAS"
SAMX = "SAMX"
MAS = "MAS"
SAM = "SAM"


################################################################################

def _get_positive_diagonals(lines: Tuple[str, ...]) -> Tuple[str, ...]:
    """

    :param lines:
    :return:
    """

    diagonals = []

    for row_start in range(len(lines)):
        line = ""
        for row in reversed(range(row_start + 1)):
            column = row_start - row
            if column < len(lines[0]):
                line += lines[row][column]
            else:
                break
        diagonals.append(line)

    row_start = len(lines) - 1
    for column_start in range(1, len(lines[0])):
        line = ""
        for row in reversed(range(row_start + 1)):
            column = row_start - row + column_start
            if column < len(lines[0]):
                line += lines[row][column]
            else:
                break
        diagonals.append(line)

    return tuple(diagonals)


################################################################################

def _get_negative_diagonals(lines: Tuple[str, ...]) -> Tuple[str, ...]:
    """

    :param lines:
    :return:
    """

    diagonals = []

    for row_start in reversed(range(len(lines))):
        line = ""
        for row in range(row_start, len(lines)):
            column = row - row_start
            if column < len(lines[0]):
                line += lines[row][column]
            else:
                break
        diagonals.append(line)

    for column_start in range(1, len(lines[0])):
        line = ""
        for row in range(len(lines)):
            column = column_start + row
            if column < len(lines[0]):
                line += lines[row][column]
            else:
                break
        diagonals.append(line)

    return tuple(diagonals)


################################################################################

def _get_vertical_lines(lines: Tuple[str, ...]) -> Tuple[str, ...]:
    """

    :param lines:
    :return:
    """

    vertical_lines = []

    for column in range(len(lines[0])):
        line = ""
        for row in range(len(lines)):
            line += lines[row][column]
        vertical_lines.append(line)

    return tuple(vertical_lines)


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

    return (leg_1 == MAS or leg_1 == SAM) and (leg_2 == MAS or leg_2 == SAM)


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines_original = tuple(f.readlines())
        lines_combined = lines_original + \
                         _get_positive_diagonals(lines_original) + \
                         _get_negative_diagonals(lines_original) + \
                         _get_vertical_lines(lines_original)
        return sum(len(compile(XMAS).findall(line))
                   + len(compile(SAMX).findall(line))
                   for line in lines_combined)


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = tuple(f.readlines())
        count = 0
        for row in range(len(lines) - 2):
            for column in range(len(lines[row]) - 2):
                if _is_x_mas(row, column, lines):
                    count += 1
        return count

################################################################################
