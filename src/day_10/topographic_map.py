from typing import Dict, Tuple


class TopographicMap:
    # INPUT_FILE_PATH = "src/day_10/input.txt"
    INPUT_FILE_PATH = "src/day_10/input_test.txt"
    TRAILHEAD_HEIGHT = 0

################################################################################

    def __init__(self):
        """

        """

        self._topographic_map = None
        self._width = -1
        self._height = -1
        self._trailheads = dict()
        self._hiking_trails = []
        self._load_map()
        self._load_trailheads()

################################################################################

    @property
    def trailheads(self) -> Dict[Tuple[int, int], int]:
        """

        :return:
        """

        return self._trailheads

################################################################################

    def make_trails(self) -> None:
        """

        :return:
        """

        pass

################################################################################

    def _load_map(self) -> None:
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._topographic_map = list(list(map(int, list(line.strip())))
                                         for line in f.readlines())
            self._width = len(self._topographic_map[0])
            self._height = len(self._topographic_map)

################################################################################

    def _load_trailheads(self) -> None:
        """

        """

        for row in range(self._height):
            for column in range(self._width):
                height = self._topographic_map[row][column]
                if height == self.TRAILHEAD_HEIGHT:
                    self._trailheads[(row, column)] = 0

################################################################################

    def _get_neighbours(self, row: int, column: int) -> Tuple[Tuple[int, int]]:
        """

        :param row:
        :param column:
        :return:
        """

        neighbours = []
        if row > 0:
            # up
            neighbours.append((row - 1, column))
        if row < self._height - 1:
            # down
            neighbours.append((row + 1, column))
        if column > 0:
            # left
            neighbours.append((row, column - 1))
        if column < self._width - 1:
            # right
            neighbours.append((row, column + 1))
        return tuple(neighbours)

################################################################################
