__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import List, Tuple

"""

"""

# INPUT_FILE_PATH = "src/day_10/input.txt"
INPUT_FILE_PATH = "src/day_10/input_test.txt"


################################################################################

def _load_topographic_map() -> List[List[int]]:
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        return list(list(map(int, list(line.strip())))
                    for line in f.readlines())


################################################################################

def _get_trailheads(topographic_map: List[List[int]]) -> List[Tuple[int, int]]:
    """

    :param topographic_map:
    :return:
    """

    return list((row, column)
                for row in range(len(topographic_map))
                for column in range(len(topographic_map[row]))
                if topographic_map[row][column] == 0)


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    topographic_map = _load_topographic_map()
    print(_get_trailheads(topographic_map))
    return -1


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    return -1

################################################################################
