class PrototypeLab:
    INPUT_FILE_PATH = "src/day_06/input.txt"
    GUARD = "^"
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
        self._guard_row = None
        self._guard_column = None
        self._load_map()
        self._direction = self.START_DIRECTION
        self._placed_obstruction_row = None
        self._placed_obstruction_column = None
        self._guard_stuck_in_loop = False

################################################################################

    @property
    def map_width(self) -> int:
        """

        :return:
        """

        return len(self._map[0])

################################################################################

    @property
    def map_height(self) -> int:
        """

        :return:
        """

        return len(self._map)

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

    def print_map(self) -> None:
        """

        """

        print("====================================")
        for row in range(len(self._map)):
            print("".join(self._map[row]))
        print("====================================")

################################################################################

    def is_free_space(self, row: int, column: int) -> bool:
        """

        :param row:
        :param column:
        :return:
        """

        return self._map[row][column] == self.FREE_SPACE

################################################################################

    @property
    def free_space_count(self) -> int:
        """

        :return:
        """

        return sum("".join(row).count(self.FREE_SPACE) for row in self._map)

################################################################################

    def walk_guard(self) -> None:
        """

        """

        while self.guard_inside_map and not self._guard_stuck_in_loop:
            self._move_guard()

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

            for i in range(len(self._map)):
                row = self._map[i]

                if self.GUARD in row:
                    self._guard_row = i
                    self._guard_column = row.index(self.GUARD)
                    break

################################################################################

    def _move_guard(self) -> None:
        """

        """

        look_ahead_row = self.DIRECTIONS[self._direction][self.MOVE_ROW](self._guard_row)
        look_ahead_column = self.DIRECTIONS[self._direction][self.MOVE_COLUMN](self._guard_column)

        if (0 <= look_ahead_row < self.map_height
                and 0 <= look_ahead_column < self.map_width):
            look_ahead_place = self._map[look_ahead_row][look_ahead_column]
            if look_ahead_place == self.OBSTRUCTION:
                self._direction = self.DIRECTIONS[self._direction][self.TURN]
            elif look_ahead_place == self._direction:
                self._guard_stuck_in_loop = True
            else:
                self._guard_row = look_ahead_row
                self._guard_column = look_ahead_column
            self._map[self._guard_row][self._guard_column] = self._direction
        else:
            self._guard_row = None
            self._guard_column = None

################################################################################
