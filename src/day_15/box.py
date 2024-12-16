__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"


class Box:

    def __init__(self, row: int, column: int):
        """

        :param row:
        :param column:
        """

        self._row = row
        self._column = column

################################################################################

    @property
    def row(self) -> int:
        """

        :return:
        """

        return self._row

################################################################################

    @property
    def column(self) -> int:
        """

        :return:
        """

        return self._column

################################################################################

    @property
    def gps_coordinate(self) -> int:
        """

        :return:
        """

        return 100 * self._row + self._column

################################################################################

    def move_left(self) -> None:
        """

        """

        self._column -= 1

################################################################################

    def move_right(self) -> None:
        """

        """

        self._column += 1

################################################################################

    def move_up(self) -> None:
        """

        """

        self._row -= 1

################################################################################

    def move_down(self) -> None:
        """

        """

        self._row += 1

################################################################################
