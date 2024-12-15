__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Self


################################################################################

class Robot:

    def __init__(self,
                 pos_x: int, pos_y: int,
                 v_x: int, v_y: int,
                 hall_width: int, hall_height: int):
        """
        :param pos_x: the number of tiles the robot is from the left wall
        :param pos_y: the number of tiles from the top wall
        :param v_x: horizontal velocity, tiles per second; positive value means
        the robot is moving to the right
        :param v_y: vertical velocity, tiles per second; positive value means
        the robot is moving down
        :param hall_width: hall width in tiles
        :param hall_height: hall height in tiles
        """

        self._pos_x = pos_x
        self._pos_y = pos_y
        self._v_x = v_x
        self._v_y = v_y
        self._hall_width = hall_width
        self._hall_height = hall_height

################################################################################

    @property
    def pos_x(self) -> int:
        """
        :return: the number of tiles the robot is from the left wall
        """

        return self._pos_x

################################################################################

    @property
    def pos_y(self) -> int:
        """
        :return: the number of tiles from the top wall
        """

        return self._pos_y

################################################################################

    def move(self) -> None:
        """
        One second elapses; move the robot according to its horizontal and
        vertical velocity. Account for the teleportation instead of crashing
        into a wall (wrap-around).
        """

        self._pos_x += self._v_x
        self._pos_x %= self._hall_width
        self._pos_y += self._v_y
        self._pos_y %= self._hall_height

################################################################################

    def __eq__(self, other: Self):
        """
        :param other: other robot to compare with
        :return: True if this and the other robot are on the same position,
        False otherwise
        """

        if isinstance(other, self.__class__):
            return self._pos_x == other.pos_x and self._pos_y == other.pos_y
        else:
            return False

################################################################################
