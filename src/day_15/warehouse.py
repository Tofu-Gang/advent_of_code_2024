__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from .movable_object import MovableObject
from .box import Box


class Warehouse:
    INPUT_FILE_PATH = "src/day_15/input.txt"
    MAP_ELEMENTS_NORMAL = "NORMAL"
    MAP_ELEMENTS_WIDE = "WIDE"
    # what is in the input file
    WALL = "#"
    BOX = "O"
    ROBOT = "@"
    EMPTY_SPACE = "."
    # what goes in the map
    MAP_ELEMENTS = {
        MAP_ELEMENTS_NORMAL: {
            WALL: "#",
            BOX: "O",
            ROBOT: "@",
            EMPTY_SPACE: "."
        },
        MAP_ELEMENTS_WIDE: {
            WALL: "##",
            BOX: "[]",
            ROBOT: "@.",
            EMPTY_SPACE: ".."
        }
    }

    LEFT = "<"
    RIGHT = ">"
    UP = "^"
    DOWN = "v"

    ROW = "ROW"
    COLUMN = "COLUMN"
    MOVE = "MOVE"
    NEIGHBOURING = "NEIGHBOURING"

    DIRECTIONS = {
        LEFT: {
            ROW: lambda row: row,
            COLUMN: lambda column: column - 1,
            MOVE: lambda movable: movable.move_left(),
            NEIGHBOURING: lambda movable: movable.neighbouring_left()
        },
        RIGHT: {
            ROW: lambda row: row,
            COLUMN: lambda column: column + 1,
            MOVE: lambda movable: movable.move_right(),
            NEIGHBOURING: lambda movable: movable.neighbouring_right()
        },
        UP: {
            ROW: lambda row: row - 1,
            COLUMN: lambda column: column,
            MOVE: lambda movable: movable.move_up(),
            NEIGHBOURING: lambda movable: movable.neighbouring_up()
        },
        DOWN: {
            ROW: lambda row: row + 1,
            COLUMN: lambda column: column,
            MOVE: lambda movable: movable.move_down(),
            NEIGHBOURING: lambda movable: movable.neighbouring_down()
        }
    }

################################################################################

    def __init__(self, map_elements: str):
        """

        """

        self._map_elements = self.MAP_ELEMENTS[map_elements]
        self._map = []
        self._boxes = []
        self._robot = None
        self._instructions = []
        self._load_input_file()

################################################################################

    @property
    def gps_coordinates_sum(self) -> int:
        """

        :return:
        """

        return sum(box.gps_coordinate for box in self._boxes)

################################################################################

    def process_instructions(self) -> None:
        """

        """

        while len(self._instructions) > 0:
            self._process_instruction()

################################################################################

    def _load_input_file(self) -> None:
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            contents = f.read().strip().split("\n\n")
            warehouse_map = contents[0].strip().split("\n")
            box_width = len(self._map_elements[self.BOX])

            for i in range(len(warehouse_map)):
                line = warehouse_map[i]
                self._map.append([])

                for j in range(len(line.strip())):
                    map_element = line[j]

                    if map_element == self.WALL or map_element == self.EMPTY_SPACE:
                        self._map[i] += list(self._map_elements[map_element])
                    elif map_element == self.ROBOT:
                        self._robot = MovableObject(i, j * box_width)
                        self._map[i] += list(self._map_elements[self.EMPTY_SPACE])
                    elif map_element == self.BOX:
                        self._boxes.append(Box(i, j * box_width, box_width))
                        self._map[i] += list(self._map_elements[self.EMPTY_SPACE])

            self._instructions = list("".join(contents[1].strip().split("\n")))

################################################################################

    def _process_instruction(self) -> None:
        """

        """

        instruction = self._instructions.pop(0)
        objects_to_move = [self._robot]
        directions = self.DIRECTIONS[instruction]
        neighbourings = directions[self.NEIGHBOURING](self._robot)

        while len(neighbourings) > 0:
            neighbouring = neighbourings.pop()
            row = neighbouring[0]
            column = neighbouring[1]
            box = self._get_box(row, column)

            if box is not None:
                objects_to_move.append(box)
                neighbourings += directions[self.NEIGHBOURING](box)
            else:
                if self._map[row][column] == self.WALL:
                    objects_to_move.clear()
                    break

        for object_to_move in tuple(set(objects_to_move)):
            directions[self.MOVE](object_to_move)

################################################################################

    def _get_box(self, row: int, column: int) -> Box | None:
        """

        :param row:
        :param column:
        :return:
        """

        try:
            return next(filter(
                lambda box: box.is_on_position(row, column),
                self._boxes))
        except StopIteration:
            return None

################################################################################
