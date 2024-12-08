__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from .city_map import CityMap

INPUT_FILE_PATH = "src/day_08/input.txt"


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    city_map = CityMap()
    city_map.print_map()
    return len(city_map.antinodes)


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    return -1

################################################################################
