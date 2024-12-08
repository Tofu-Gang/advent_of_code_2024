__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from .city_map import CityMap


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    city_map = CityMap(False)
    return len(city_map.antinodes)


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    city_map = CityMap(True)
    return len(city_map.antinodes)

################################################################################
