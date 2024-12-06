__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from .prototype_lab import PrototypeLab


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    prototype_lab = PrototypeLab()
    prototype_lab.walk_guard()
    return prototype_lab.visited_positions


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    solutions_count = 0
    prototype_lab = PrototypeLab()
    attempt_count = 0

    for row in range(prototype_lab.map_height):
        for column in range(prototype_lab.map_width):
            if prototype_lab.is_free_space(row, column):
                attempt_count += 1
                prototype_lab.place_obstruction(row, column)
                prototype_lab.walk_guard()

                if prototype_lab.guard_stuck_in_loop:
                    solutions_count += 1
                    print(f"{attempt_count}/{prototype_lab.free_space_count}")
                prototype_lab.reset_map()
    return solutions_count
    # return -1

################################################################################
