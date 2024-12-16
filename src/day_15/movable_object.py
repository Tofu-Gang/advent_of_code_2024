__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple


class MovableObject:

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

    def neighbouring_left(self):
        """

        :return:
        """

        return [(self._row, self._column - 1)]

################################################################################

    def neighbouring_right(self):
        """

        :return:
        """

        return [(self._row, self._column + 1)]

################################################################################

    def neighbouring_up(self):
        """

        :return:
        """

        return [(self._row - 1, self._column)]

################################################################################

    def neighbouring_down(self):
        """

        :return:
        """

        return [(self._row + 1, self._column)]

################################################################################
