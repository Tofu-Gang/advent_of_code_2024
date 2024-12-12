__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from .topographic_map import TopographicMap


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    topographic_map = TopographicMap()
    topographic_map.make_trails()
    return topographic_map.scores_sum


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    topographic_map = TopographicMap()
    topographic_map.make_trails()
    return topographic_map.ratings_sum

################################################################################
