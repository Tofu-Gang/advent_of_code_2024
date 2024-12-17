from typing import Tuple


class PrototypeLab:
    INPUT_FILE_PATH = "src/day_06/input.txt"
    OBSTRUCTION = "#"
    FREE_SPACE = "."
    NORTH = "^"
    SOUTH = "v"
    EAST = ">"
    WEST = "<"
    TURN = "TURN"
    MOVE_ROW = "MOVE_ROW"
    MOVE_COLUMN = "MOVE_COLUMN"
    START_DIRECTION = NORTH

    DIRECTIONS = {
        NORTH: {
            TURN: EAST,
            MOVE_ROW: lambda row: row - 1,
            MOVE_COLUMN: lambda column: column
        },
        SOUTH: {
            TURN: WEST,
            MOVE_ROW: lambda row: row + 1,
            MOVE_COLUMN: lambda column: column
        },
        EAST: {
            TURN: SOUTH,
            MOVE_ROW: lambda row: row,
            MOVE_COLUMN: lambda column: column + 1
        },
        WEST: {
            TURN: NORTH,
            MOVE_ROW: lambda row: row,
            MOVE_COLUMN: lambda column: column - 1
        }
    }

################################################################################

    def __init__(self):
        """

        """

        self._map = None
        self._width = -1
        self._height = -1

        self._guard_start_row = None
        self._guard_start_column = None
        self._guard_row = None
        self._guard_column = None
        self._direction = self.START_DIRECTION
        self._guard_stuck_in_loop = False
        self._new_visited_tiles = -1

        self._relevant_obstructions_positions = None
        self._placed_obstruction_row = None
        self._placed_obstruction_column = None

        self._load_map()
        self._get_relevant_obstructions_positions()

################################################################################

    @property
    def visited_position_count(self) -> int:
        """

        :return:
        """

        return sum("".join(row).count(symbol)
                   for row in self._map
                   for symbol in self.DIRECTIONS)

################################################################################

    def make_round(self) -> None:
        """

        """

        while True:
            directions = self.DIRECTIONS[self._direction]
            next_row = directions[self.MOVE_ROW](self._guard_row)
            next_column = directions[self.MOVE_COLUMN](self._guard_column)

            if 0 <= next_row < self._height and 0 <= next_column < self._width:
                next_tile = self._map[next_row][next_column]

                if next_tile == self._direction:
                    self._guard_stuck_in_loop = True
                    break
                elif next_tile == self.OBSTRUCTION:
                    self._direction = directions[self.TURN]
                else:
                    self._guard_row = next_row
                    self._guard_column = next_column

                    if self._guard_row == self._guard_start_row and self._guard_column == self._guard_start_column:
                        if self._new_visited_tiles == 0:
                            self._guard_stuck_in_loop = True
                            break
                        else:
                            self._new_visited_tiles = 0
                    if next_tile == self.FREE_SPACE:
                        self._new_visited_tiles += 1
                    self._map[self._guard_row][
                        self._guard_column] = self._direction
            else:
                # guard stepped outside the map
                break

################################################################################

    def make_rounds_with_new_obstructions(self) -> int:
        """

        :return:
        """

        solutions_count = 0

        for obstruction_position in self._relevant_obstructions_positions:
            self._place_obstruction(obstruction_position[0], obstruction_position[1])
            self.make_round()

            if self._guard_stuck_in_loop:
                solutions_count += 1
            self._reset_map()
        return solutions_count

################################################################################

    def _place_obstruction(self, row: int, column: int) -> None:
        """

        :param row:
        :param column:
        """

        self._placed_obstruction_row = row
        self._placed_obstruction_column = column
        self._map[self._placed_obstruction_row][self._placed_obstruction_column] = self.OBSTRUCTION

################################################################################

    def _reset_map(self) -> None:
        """

        """

        try:
            self._map[self._placed_obstruction_row][self._placed_obstruction_column] = self.FREE_SPACE
            self._placed_obstruction_row = None
            self._placed_obstruction_column = None
        except TypeError:
            pass

        self._direction = self.START_DIRECTION
        self._guard_row = self._guard_start_row
        self._guard_column = self._guard_start_column
        self._guard_stuck_in_loop = False

        for row in range(self._height):
            for column in range(self._width):
                tile = self._map[row][column]

                if tile in self.DIRECTIONS:
                    self._map[row][column] = self.FREE_SPACE
        self._map[self._guard_row][self._guard_column] = self._direction
        self._new_visited_tiles = 1

################################################################################

    def _load_map(self) -> None:
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._map = list(list(row.strip()) for row in f.readlines())
            self._height = len(self._map)
            self._width = len(self._map[0])

            for i in range(len(self._map)):
                row = self._map[i]

                if self.START_DIRECTION in row:
                    self._guard_start_row = i
                    self._guard_start_column = row.index(self.START_DIRECTION)
                    self._guard_row = i
                    self._guard_column = row.index(self.START_DIRECTION)
                    self._new_visited_tiles = 1
                    break

################################################################################

    def _get_relevant_obstructions_positions(self) -> None:
        """

        :return:
        """

        self._reset_map()
        self.make_round()
        self._relevant_obstructions_positions = tuple(
            (row, column)
            for row in range(self._height)
            for column in range(self._width)
            if self._map[row][column] in self.DIRECTIONS)

################################################################################
