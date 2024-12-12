__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import List

"""

"""

INPUT_FILE_PATH = "src/day_11/input.txt"
# INPUT_FILE_PATH = "src/day_11/input_test.txt"


################################################################################

def _load_stones() -> List[int]:
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        return list(map(int, f.read().strip().split()))


################################################################################

def _process_stone(stone: int, result: int, blinks: int, goal: int) -> int:
    """

    :param stone:
    :param result:
    :param blinks:
    :return:
    """

    if blinks == goal:
        return result
    elif stone == 0:
        return _process_stone(1, result, blinks + 1, goal)
    elif len(str(stone)) % 2 == 0:
        half = int(len(str(stone)) / 2)
        left = int(str(stone)[:half])
        right = int(str(stone)[half:])
        return (_process_stone(left, result, blinks + 1, goal)
                + _process_stone(right, result, blinks + 1, goal))
    else:
        return _process_stone(stone * 2024, result, blinks + 1, goal)


################################################################################

def puzzle_01() -> int:
    """

    :return:
    """

    stones = _load_stones()
    result = 0
    for stone in stones:
        result += _process_stone(stone, 1, 0, 25)
    return result


################################################################################

def puzzle_02() -> int:
    """

    :return:
    """

    return -1

################################################################################
