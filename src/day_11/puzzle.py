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

def _blink(stones: List[int]) -> List[int]:
    """

    :param stones:
    :return:
    """

    i = 0

    while True:
        stone = stones[i]

        if stone == 0:
            stones[i] = 1
            i += 1
        elif len(str(stone)) % 2 == 0:
            left = int(str(stone)[:int(len(str(stone)) / 2)])
            right = int(str(stone)[int(len(str(stone)) / 2):])
            stones[i] = left
            stones.insert(i + 1, right)
            i += 2
        else:
            stones[i] = stone * 2024
            i += 1

        if i == len(stones):
            break

    return stones


################################################################################

def puzzle_01() -> int:
    """

    :return:
    """

    stones = _load_stones()

    for i in range(25):
        print(i)
        stones = _blink(stones)
    print(len(stones))
    return -1


################################################################################

def puzzle_02() -> int:
    """

    :return:
    """

    return -1

################################################################################
