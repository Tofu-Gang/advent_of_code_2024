from typing import Self, List


class Node:

    def __init__(self, row: int, column: int, parent: Self | None):

        self._row = row
        self._column = column
        self._parent = parent
        self._children = []

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
    def children(self) -> List[Self]:
        """

        :return:
        """

        return self._children

################################################################################

    @property
    def parent_node(self) -> Self | None:
        """

        :return:
        """

        return self._parent

################################################################################

    @property
    def trailhead(self) -> Self:
        """

        :return:
        """

        node = self

        while node.parent_node is not None:
            node = node.parent_node

        return node

################################################################################

    def add_child(self, child: Self) -> None:
        """

        """

        self._children.append(child)

################################################################################
