class PrototypeLab:
    INPUT_FILE_PATH = "src/day_06/input.txt"
    GUARD = "^"
    OBSTRUCTION = "#"
    VISITED = "X"
    FREE_SPACE = "."
    NORTH = "^"
    SOUTH = "v"
    EAST = ">"
    WEST = "<"
    TURN = "TURN"
    MOVE_ROW = "MOVE_ROW"
    MOVE_COLUMN = "MOVE_COLUMN"

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
        self._direction = self.NORTH

################################################################################

    def walk_guard(self) -> None:
        """

        """

        while self.guard_inside_map:
            self._move_guard()

################################################################################

    @property
    def guard_inside_map(self) -> bool:
        """

        :return:
        """

        return self._guard_row is not None and self._guard_column is not None

################################################################################

    @property
    def visited_positions(self) -> int:
        """

        :return:
        """

        return sum("".join(row).count(self.VISITED) for row in self._map)

################################################################################

    def _load_map(self) -> None:
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._map = list(list(row) for row in f.readlines())

            for i in range(len(self._map)):
                row = self._map[i]

                if self.GUARD in row:
                    self._guard_row = i
                    self._guard_column = row.index(self.GUARD)
                    self._map[i][self._guard_column] = self.VISITED
                    break

################################################################################

    def _move_guard(self) -> None:
        """

        """

        look_ahead_row = self.DIRECTIONS[self._direction][self.MOVE_ROW](self._guard_row)
        look_ahead_column = self.DIRECTIONS[self._direction][self.MOVE_COLUMN](self._guard_column)
        try:
            if self._map[look_ahead_row][look_ahead_column] == self.OBSTRUCTION:
                self._direction = self.DIRECTIONS[self._direction][self.TURN]
            else:
                self._guard_row = look_ahead_row
                self._guard_column = look_ahead_column
        except IndexError:
            self._guard_row = None
            self._guard_column = None

        try:
            self._map[self._guard_row][self._guard_column] = self.VISITED
        except TypeError:
            pass

################################################################################

