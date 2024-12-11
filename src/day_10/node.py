from typing import Self


class Node:

    def __init__(self, row: int, column: int, height: int, parent: Self | None):
        """

        :param row:
        :param column:
        :param height:
        """

        self._row = row
        self._column = column
        self._height = height
        self._parent = None