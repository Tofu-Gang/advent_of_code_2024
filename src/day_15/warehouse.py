__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from .box import Box
from .robot import Robot


class Warehouse:
    INPUT_FILE_PATH = "src/day_15/input.txt"
    # INPUT_FILE_PATH = "src/day_15/input_test.txt"
    # INPUT_FILE_PATH = "src/day_15/input_test_small.txt"
    WALL = "#"
    BOX = "O"
    ROBOT = "@"
    EMPTY_SPACE = "."
    RIGHT = ">"
    UP = "^"
    LEFT = "<"
    DOWN = "v"

################################################################################

    def __init__(self):
        """

        """

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

        for box in self._boxes:
            map_copy[box.row][box.column] = self.BOX
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
            for i in range(len(warehouse_map)):
                line = warehouse_map[i]
                self._map.append([])

                for j in range(len(line.strip())):
                    space = line[j]

                    if space == self.WALL or space == self.EMPTY_SPACE:
                        self._map[i].append(line[j])
                    elif space == self.ROBOT:
                        self._robot = Robot(i, j)
                        self._map[i].append(self.EMPTY_SPACE)
                    elif space == self.BOX:
                        self._boxes.append(Box(i, j))
                        self._map[i].append(self.EMPTY_SPACE)

            self._instructions = list(contents[1].strip())

################################################################################

    def _process_instruction(self) -> None:
        """

        """

        instruction = self._instructions.pop(0)
        row = self._robot.row
        column = self._robot.column
        objects_to_move = [self._robot]

        while True:
            if instruction == self.RIGHT:
                column += 1
            elif instruction == self.LEFT:
                column -= 1
            elif instruction == self.UP:
                row -= 1
            elif instruction == self.DOWN:
                row += 1

            neighbour = self._map[row][column]

            try:
                objects_to_move.append(next(filter(
                    lambda box: box.row == row and box.column == column,
                    self._boxes)))
            except StopIteration:
                if neighbour == self.WALL:
                    objects_to_move.clear()
                    break
                elif neighbour == self.EMPTY_SPACE:
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

################################################################################
