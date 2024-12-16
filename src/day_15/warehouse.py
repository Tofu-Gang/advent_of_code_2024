__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from .box import Box
from .robot import Robot


class Warehouse:
    # INPUT_FILE_PATH = "src/day_15/input.txt"
    # INPUT_FILE_PATH = "src/day_15/input_test.txt"
    # INPUT_FILE_PATH = "src/day_15/input_test_small.txt"
    INPUT_FILE_PATH = "src/day_15/input_test_2.txt"
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

    RIGHT = ">"
    UP = "^"
    LEFT = "<"
    DOWN = "v"

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

    def print_map(self) -> None:
        """

        :return:
        """

        map_copy = list(line.copy() for line in self._map)
        map_copy[self._robot.row][self._robot.column] = self.ROBOT
        box_width = len(self._map_elements[self.BOX])

        for box in self._boxes:
            map_copy[box.row][box.column:box.column + box_width] = list(self._map_elements[self.BOX])
        for line in map_copy:
            print("".join(line))

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
                        self._robot = Robot(i, j * box_width)
                        self._map[i] += list(self._map_elements[self.EMPTY_SPACE])
                    elif map_element == self.BOX:
                        self._boxes.append(Box(i, j * box_width, box_width))
                        self._map[i] += list(self._map_elements[self.EMPTY_SPACE])

            self._instructions = list(contents[1].strip())

################################################################################

    def _process_instruction(self) -> None:
        """

        """

        instruction = self._instructions.pop(0)
        print(instruction)
        row = self._robot.row
        column = self._robot.column
        objects_to_move = [self._robot]

        if instruction == self.RIGHT:
            column += 1
        elif instruction == self.LEFT:
            column -= 1
        elif instruction == self.UP:
            row -= 1
        elif instruction == self.DOWN:
            row += 1

        while True:
            box = self._get_box(row, column)
            if box is not None:
                if self._can_box_be_moved(box, instruction):
                    objects_to_move.append(box)

                    if instruction == self.RIGHT:
                        column += box.width
                    elif instruction == self.LEFT:
                        column -= box.width
                    elif instruction == self.UP:
                        row -= 1
                    elif instruction == self.DOWN:
                        row += 1
                else:
                    objects_to_move.clear()
                    break
            else:
                if self._map[row][column] == self.WALL:
                    objects_to_move.clear()
                    break
                elif self._map[row][column] == self.EMPTY_SPACE:
                    break

        for object_to_move in objects_to_move:
            if instruction == self.RIGHT:
                object_to_move.move_right()
            elif instruction == self.LEFT:
                object_to_move.move_left()
            elif instruction == self.UP:
                object_to_move.move_up()
            elif instruction == self.DOWN:
                object_to_move.move_down()
        self.print_map()

################################################################################

    def _get_box(self, row: int, column: int) -> Box | None:
        """

        :param row:
        :param column:
        :return:
        """

        try:
            return next(filter(
                lambda box:
                box.row == row and
                (box.column == column or box.column + box.width - 1 == column),
                self._boxes))
        except StopIteration:
            return None

################################################################################

    def _can_box_be_moved(self, box: Box, direction: str) -> bool:
        """

        :param box:
        :param direction:
        :return:
        """

        row = box.row
        column = box.column

        if direction == self.RIGHT:
            column = box.column + box.width
        elif direction == self.LEFT:
            column = box.column - 1
        elif direction == self.UP:
            row = box.row - 1
        elif direction == self.DOWN:
            row = box.row + 1

        if self._map[row][column] == self.WALL:
            return False
        else:
            try:
                box = self._get_box(row, column)
                return self._can_box_be_moved(box, direction)
            except AttributeError:
                return True


################################################################################
