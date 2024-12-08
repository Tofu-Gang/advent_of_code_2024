class Antenna:

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
