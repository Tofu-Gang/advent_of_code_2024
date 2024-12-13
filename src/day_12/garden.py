from locale import str

from .region import Region


class Garden:
    # INPUT_FILE_PATH = "src/day_12/input.txt"
    INPUT_FILE_PATH = "src/day_12/input_test.txt"

    ROW_KEY = "ROW"
    COLUMN_KEY = "COLUMN"
    DIRECTIONS = {
        0: {
            ROW_KEY: lambda row: row,
            COLUMN_KEY: lambda column: column + 1
        },
        1: {
            ROW_KEY: lambda row: row - 1,
            COLUMN_KEY: lambda column: column + 1
        },
        2: {
            ROW_KEY: lambda row: row - 1,
            COLUMN_KEY: lambda column: column
        },
        3: {
            ROW_KEY: lambda row: row - 1,
            COLUMN_KEY: lambda column: column - 1
        },
        4: {
            ROW_KEY: lambda row: row,
            COLUMN_KEY: lambda column: column - 1
        },
        5: {
            ROW_KEY: lambda row: row + 1,
            COLUMN_KEY: lambda column: column - 1
        },
        6: {
            ROW_KEY: lambda row: row + 1,
            COLUMN_KEY: lambda column: column
        },
        7: {
            ROW_KEY: lambda row: row + 1,
            COLUMN_KEY: lambda column: column + 1
        }
    }

################################################################################

    def __init__(self):
        """

        """

        self._plots_map = None
        self._map_height = -1
        self._map_width = -1
        self._regions = []
        self._plants = None
        self._load_map()
        self._load_plants()
        self._load_regions()

################################################################################

    @property
    def fence_price(self) -> int:
        """

        :return:
        """

        return sum(region.fence_price for region in self._regions)

################################################################################

    def _freeman_code(self, plant) -> str:
        """
        3  2  1
         \ | /
        4-- --0
         / | \
        5  6  7

        :param plant:
        :return:
        """

        direction = 0
        start = None
        code = ""

        for row in range(self._map_height):
            for column in range(self._map_width):
                plot = self._plots_map[row][column]
                if plot == plant:
                    start = (row, column)
                    break
            if start is not None:
                break

        start_row = start[0]
        start_column = start[1]
        current = start

        # print(f"found start: {start_row}, {start_column}")

        while True:
            current_row = current[0]
            current_column = current[1]
            # print(f"current: {current_row}, {current_column}")
            direction = (direction + 7) % 8

            while True:
                next_row = self.DIRECTIONS[direction][self.ROW_KEY](current_row)
                next_column = self.DIRECTIONS[direction][self.COLUMN_KEY](current_column)
                # print(f"trying direction: {direction}; next: {next_row}, {next_column}")

                if next_row == start_row and next_column == start_column:
                    # print("found start here!")
                    code += str(direction)
                    return code
                elif 0 <= next_row < self._map_height and 0 <= next_column < self._map_width:
                    if self._plots_map[next_row][next_column] == plant:
                        # print("found correct plot")
                        code += str(direction)
                        current = (next_row, next_column)
                        break
                    else:
                        # print("no luck here, try new direction")
                        direction = (direction + 1) % 8
                else:
                    direction = (direction + 1) % 8
                    # print(f"out of bounds; trying {direction}")

################################################################################

    def fixed_freeman_code(self, plant: str) -> str:
        """

        :return:
        """

        code = list(map(int, list(self._freeman_code(plant).replace("1", "02").replace("3", "42").replace("5", "46").replace("7", "06"))))
        i = 0
        while True:
            try:
                current_direction = code[i]
                next_direction = code[i + 1]
                if next_direction == current_direction:
                    code.pop(i + 1)
                else:
                    if abs(current_direction - next_direction) > 2:
                        code.insert(i + 1, max(current_direction, next_direction) - 2)
                    else:
                        i += 1
            except IndexError:
                if abs(code[0] - code[-1]) > 2:
                    code.append(max(code[0], code[-1]) - 2)
                else:
                    return "".join(list(map(str, code)))

################################################################################

    def _load_map(self) -> None:
        """

        :return:
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._plots_map = list(list(line.strip()) for line in f.readlines())
            self._map_height = len(self._plots_map)
            self._map_width = len(self._plots_map[0])

################################################################################

    def _load_plants(self) -> None:
        """

        :return:
        """

        self._plants = tuple(set(sum(list(row for row in self._plots_map), [])))

################################################################################

    def _load_regions(self) -> None:
        """

        :return:
        """

        for plant in self._plants:
            plots = self._plant_plots(plant)

            while len(plots) > 0:
                region = Region(plant)
                plot = plots.pop(0)
                region.add_plot(plot[0], plot[1])

                while True:
                    for i in range(len(plots)):
                        plot = plots[i]

                        if region.belongs(plant, plot[0], plot[1]):
                            region.add_plot(plot[0], plot[1])
                            plots.pop(i)
                            break
                    else:
                        break
                self._regions.append(region)

################################################################################

    def _plant_plots(self, plant: str):
        """

        :param plant:
        :return:
        """

        return list((row, column)
                    for row in range(self._map_height)
                    for column in range(self._map_width)
                    if self._plots_map[row][column] == plant)

################################################################################
