from itertools import permutations
from typing import Tuple

from .antenna import Antenna
from .antinode import Antinode


class CityMap:
    INPUT_FILE_PATH = "src/day_08/input.txt"
    # INPUT_FILE_PATH = "src/day_08/input_test.txt"
    FREE_SPACE = "."

################################################################################
    def __init__(self):
        """

        """

        self._map_width = -1
        self._map_height = -1
        self._antennas = dict()
        self._antinodes = list()
        self._load_map()
        self._get_antinodes()

################################################################################

    @property
    def antinodes(self) -> Tuple[Antinode, ...]:
        """

        :return:
        """

        return tuple(self._antinodes)

################################################################################

    def _load_map(self) -> None:
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            lines = tuple(row.strip() for row in f.readlines())
            self._map_height = len(lines)
            self._map_width = len(lines[0])

            for row in range(len(lines)):
                for column in range(len(lines[row])):
                    place = lines[row][column]

                    if place != self.FREE_SPACE:
                        if place not in self._antennas:
                            self._antennas[place] = []
                        self._antennas[place].append(Antenna(row, column))

################################################################################

    def _get_antinode(self, antenna_1: Antenna, antenna_2: Antenna) -> [Antinode, None]:
        """

        :param antenna_1:
        :param antenna_2:
        :return:
        """

        row = antenna_1.row + (antenna_1.row - antenna_2.row)
        column = antenna_1.column + (antenna_1.column - antenna_2.column)
        antinode = Antinode(row, column)

        if (0 <= antinode.row < self._map_height
                and 0 <= antinode.column < self._map_width):
            return antinode
        else:
            return None

################################################################################

    def _get_antinodes(self) -> None:
        """

        """

        for frequency in self._antennas:
            for pair in permutations(self._antennas[frequency], 2):
                antenna_1 = pair[0]
                antenna_2 = pair[1]
                antinode = self._get_antinode(antenna_1, antenna_2)
                if antinode is not None and antinode not in self._antinodes:
                    self._antinodes.append(antinode)
                antinode = self._get_antinode(antenna_2, antenna_1)
                if antinode is not None and antinode not in self._antinodes:
                    self._antinodes.append(antinode)

################################################################################

    def print_map(self) -> None:
        """

        """

        city_map = list(list("." * self._map_width) for _ in range(self._map_height))

        for frequency in self._antennas:
            for antenna in self._antennas[frequency]:
                city_map[antenna.row][antenna.column] = frequency

        for frequency in self._antennas:
            for pair in permutations(self._antennas[frequency], 2):
                antenna_1 = pair[0]
                antenna_2 = pair[1]
                antinode = self._get_antinode(antenna_1, antenna_2)
                if antinode is not None:
                    city_map[antinode.row][antinode.column] = "#"
                antinode = self._get_antinode(antenna_2, antenna_1)
                if antinode is not None:
                    city_map[antinode.row][antinode.column] = "#"

        print("\n".join("".join(row) for row in city_map))

################################################################################
