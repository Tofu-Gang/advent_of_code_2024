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

    """
    6 3
    7 6
    7 7
    8 1
    8 3
    9 7
    """

    # prototype_lab = PrototypeLab()
    # prototype_lab.place_obstruction(11, 60)
    # prototype_lab.walk_guard()
    # print(prototype_lab.guard_stuck_in_loop)
    # return -1

    solutions_count = 0
    prototype_lab = PrototypeLab()
    attempt_count = 0

    for i in range(len(prototype_lab.potential_obstructions_positions)):
        row = prototype_lab.potential_obstructions_positions[i][0]
        column = prototype_lab.potential_obstructions_positions[i][1]
        print(f"{i}/{len(prototype_lab.potential_obstructions_positions)}")
        attempt_count += 1
        prototype_lab.place_obstruction(row, column)
        prototype_lab.walk_guard()

        if prototype_lab.guard_stuck_in_loop:
            solutions_count += 1
        prototype_lab.reset_map()
    return solutions_count

################################################################################
