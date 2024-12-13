from .region import Region


class Garden:
    INPUT_FILE_PATH = "src/day_12/input.txt"
    # INPUT_FILE_PATH = "src/day_12/input_test.txt"

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
