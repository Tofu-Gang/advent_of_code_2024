from typing import Tuple, List


class HikingTrail:

    def __init__(self, steps: Tuple[Tuple[int, int]]):
        """

        """

        self._steps = list(steps)

################################################################################

    @property
    def steps(self) -> Tuple[Tuple[int, int]]:
        """

        :return:
        """

        return tuple(self._steps)

################################################################################

    @property
    def trailhead(self) -> Tuple[int, int]:
        """

        :return:
        """

        return self._steps[0]

################################################################################

    @property
    def is_finished(self) -> bool:
        """

        :return:
        """

        return len(self._steps) == 10

################################################################################

    def add_step(self, row: int, column: int) -> None:
        """

        :param row:
        :param column:
        :return:
        """

        self._steps.append((row, column))

################################################################################
