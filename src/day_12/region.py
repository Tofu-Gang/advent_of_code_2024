class Region:

    def __init__(self, plant: str):
        """

        :param plant:
        """

        self._plant = plant
        self._plots = []

################################################################################

    @property
    def fence_price(self) -> int:
        """

        :return:
        """

        return self._area() * self._perimeter()

################################################################################

    def belongs(self, plant: str, row: int, column: int) -> bool:
        """

        :param plant:
        :param row:
        :param column:
        :return:
        """

        return plant == self._plant and any(
            neighbour in self._plots
            for neighbour in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1)))

################################################################################

    def add_plot(self, row: int, column: int) -> None:
        """

        :param row:
        :param column:
        :return:
        """

        self._plots.append((row, column))

################################################################################

    def _area(self) -> int:
        """

        :return:
        """

        return len(self._plots)

################################################################################

    def _perimeter(self) -> int:
        """

        :return:
        """

        perimeter = 0

        for plot in self._plots:
            row = plot[0]
            column = plot[1]

            if (row - 1, column) not in self._plots:
                perimeter += 1
            if (row + 1, column) not in self._plots:
                perimeter += 1
            if (row, column - 1) not in self._plots:
                perimeter += 1
            if (row, column + 1) not in self._plots:
                perimeter += 1

        return perimeter

################################################################################
