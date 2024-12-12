from typing import Tuple, List
from .node import Node


class TopographicMap:
    INPUT_FILE_PATH = "src/day_10/input.txt"
    TRAILHEAD_HEIGHT = 0

################################################################################

    def __init__(self):
        """

        """

        self._topographic_map = None
        self._width = -1
        self._height = -1
        self._trailheads = []
        self._scores = dict()
        self._ratings = dict()
        self._load_map()
        self._load_trailheads()

################################################################################

    @property
    def scores_sum(self) -> int:
        """

        :return:
        """

        return sum(len(self._scores[trailhead]) for trailhead in self._scores)

################################################################################

    @property
    def ratings_sum(self) -> int:
        """

        :return:
        """

        return sum(self._ratings[trailhead] for trailhead in self._ratings)

################################################################################

    def make_trails(self) -> None:
        """

        :return:
        """

        for trailhead in self._trailheads:
            self._process_node(trailhead)

################################################################################

    def _process_node(self, node) -> None:
        """

        :param node:
        """

        row = node.row
        column = node.column
        height = self._topographic_map[row][column]
        neighbours = self._get_neighbours(row, column)

        if height == 9:
            trailhead = node.trailhead
            if (row, column) not in self._scores[(trailhead.row, trailhead.column)]:
                self._scores[(trailhead.row, trailhead.column)].append((row, column))
            self._ratings[(trailhead.row, trailhead.column)] += 1

        else:
            for neighbour in neighbours:
                neighbour_row = neighbour[0]
                neighbour_column = neighbour[1]
                neighbour_height = self._topographic_map[neighbour_row][neighbour_column]

                if neighbour_height - 1 == height:
                    node.add_child(Node(neighbour_row, neighbour_column, node))

            if len(node.children) == 0:
                pass
            else:
                for child in node.children:
                    self._process_node(child)

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
                    self._trailheads.append(Node(row, column, None))
                    self._scores[(row, column)] = []
                    self._ratings[(row, column)] = 0

################################################################################

    def _get_neighbours(self, row: int, column: int) -> List[Tuple[int, int]]:
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
        return neighbours

################################################################################
