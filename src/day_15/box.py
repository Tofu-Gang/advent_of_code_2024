__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from .movable_object import MovableObject


class Box(MovableObject):

    def __init__(self, row: int, column: int, width: int):
        """

        :param row:
        :param column:
        """

        super().__init__(row, column)
        self._width = width

################################################################################

    @property
    def gps_coordinate(self) -> int:
        """

        :return:
        """

        return 100 * self._row + self._column

################################################################################

    def neighbouring_right(self):
        """

        :return:
        """

        if self._width == 1:
            return super().neighbouring_right()
        else:
            return [(self._row, self._column + self._width)]

################################################################################

    def neighbouring_up(self):
        """

        :return:
        """

        if self._width == 1:
            return super().neighbouring_up()
        else:
            return [(self._row - 1, self._column),
                    (self._row - 1, self._column + 1)]

################################################################################

    def neighbouring_down(self):
        """

        :return:
        """

        if self._width == 1:
            return super().neighbouring_down()
        else:
            return [(self._row + 1, self._column),
                    (self._row + 1, self._column + 1)]

################################################################################

    def is_on_position(self, row: int, column: int) -> bool:
        """

        :param row:
        :param column:
        :return:
        """

        if self._width == 1:
            return row == self._row and column == self._column
        else:
            return row == self._row and (column == self._column or column == self._column + 1)

################################################################################
