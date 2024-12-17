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

        self._load_map()
        self._potential_obstructions_positions = None
        self._placed_obstruction_row = None
        self._placed_obstruction_column = None
        self._get_potential_obstructions_positions()

################################################################################

    @property
    def guard_inside_map(self) -> bool:
        """

        :return:
        """

        return self._guard_row is not None and self._guard_column is not None

################################################################################

    @property
    def guard_stuck_in_loop(self) -> bool:
        """

        :return:
        """

        return self._guard_stuck_in_loop

################################################################################

    @property
    def visited_positions(self) -> int:
        """

        :return:
        """

        return sum(
            "".join(row).count(symbol)
            for row in self._map
            for symbol in (self.NORTH, self.SOUTH, self.EAST, self.WEST))

################################################################################

    @property
    def potential_obstructions_positions(self) -> Tuple[Tuple[int, int]]:
        """

        :return:
        """

        return self._potential_obstructions_positions

################################################################################

    def walk_guard(self) -> None:
        """

        """

        count = 0
        while self.guard_inside_map and not self._guard_stuck_in_loop:
            self._move_guard()
            count += 1
            if count == 1000000:
                self._guard_stuck_in_loop = True

################################################################################

    def place_obstruction(self, row: int, column: int) -> None:
        """

        :param row:
        :param column:
        """

        self._placed_obstruction_row = row
        self._placed_obstruction_column = column
        self._map[self._placed_obstruction_row][self._placed_obstruction_column] = self.OBSTRUCTION

################################################################################

    def reset_map(self) -> None:
        """

        """

        self._load_map()
        self._direction = self.START_DIRECTION
        self._guard_stuck_in_loop = False
        self._placed_obstruction_row = None
        self._placed_obstruction_column = None

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
                    break

################################################################################

    def _move_guard(self) -> None:
        """

        """

        look_ahead_row = self.DIRECTIONS[self._direction][self.MOVE_ROW](self._guard_row)
        look_ahead_column = self.DIRECTIONS[self._direction][self.MOVE_COLUMN](self._guard_column)

        if (0 <= look_ahead_row < self._height
                and 0 <= look_ahead_column < self._width):
            look_ahead_place = self._map[look_ahead_row][look_ahead_column]
            # if self._placed_obstruction_row == 11 and self._placed_obstruction_column == 60:
            #     visited = (sum(row.count(self.NORTH) for row in self._map) +
            #                sum(row.count(self.SOUTH) for row in self._map) +
            #                sum(row.count(self.EAST) for row in self._map) +
            #                sum(row.count(self.WEST) for row in self._map))
            #     print(f"{visited}; {self._direction} {look_ahead_place}")

            if look_ahead_place == self._direction:
                self._guard_stuck_in_loop = True
            elif look_ahead_place == self.OBSTRUCTION:
                self._direction = self.DIRECTIONS[self._direction][self.TURN]

                if self._direction == self._map[self._guard_row][self._guard_column]:
                    self._guard_stuck_in_loop = True
            else:
                self._guard_row = look_ahead_row
                self._guard_column = look_ahead_column
                if self._direction == self._map[self._guard_row][self._guard_column]:
                    self._guard_stuck_in_loop = True

            self._map[self._guard_row][self._guard_column] = self._direction
        else:
            self._guard_row = None
            self._guard_column = None

################################################################################

    def _get_potential_obstructions_positions(self) -> None:
        """

        :return:
        """

        self.reset_map()
        self.walk_guard()
        self._potential_obstructions_positions = tuple(
            (row, column)
            for row in range(self._height)
            for column in range(self._width)
            if self._map[row][column] in (self.NORTH, self.SOUTH, self.EAST, self.WEST))

################################################################################
