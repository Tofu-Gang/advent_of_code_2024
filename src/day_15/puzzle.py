__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from .warehouse import Warehouse


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    warehouse = Warehouse(Warehouse.MAP_ELEMENTS_NORMAL)
    warehouse.process_instructions()
    return warehouse.gps_coordinates_sum


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    warehouse = Warehouse(Warehouse.MAP_ELEMENTS_WIDE)
    warehouse.print_map()
    warehouse.process_instructions()
    # print(warehouse.gps_coordinates_sum)
    return -1

################################################################################