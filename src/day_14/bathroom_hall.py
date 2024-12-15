__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from re import compile
from .robot import Robot


################################################################################

class BathroomHall:
    INPUT_FILE_PATH = "src/day_14/input.txt"
    HEIGHT = 103
    WIDTH = 101

################################################################################

    def __init__(self):
        """
        Load the robots from the input file.
        """

        self._robots = []
        self._load_robots()

################################################################################

    def _load_robots(self) -> None:
        """
        Load the robots from the input file.
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            lines = list(line.strip() for line in f.readlines())
            pattern = compile(r"-?\d+")
            [self._robots.append(
                Robot(
                    *list(map(int, pattern.findall(line))),
                    self.WIDTH, self.HEIGHT))
                for line in lines]

################################################################################

    def move_robots(self, seconds: int) -> None:
        """
        Wait the specified number of seconds; move each robot accordingly.
        :param seconds: number of seconds to wait
        """

        [robot.move()
         for robot in self._robots
         for _ in range(seconds)]

################################################################################

    @property
    def safety_factor(self) -> int:
        """
        :return: Safety factor, which is a product of number of robots in each
        of four hall quadrants (not including the middle row and column)
        """

        q_1 = 0
        q_2 = 0
        q_3 = 0
        q_4 = 0

        for robot in self._robots:
            pos_x = robot.pos_x
            pos_y = robot.pos_y

            if pos_x > self.WIDTH // 2 and pos_y < self.HEIGHT // 2:
                q_1 += 1
            elif pos_x < self.WIDTH // 2 and pos_y < self.HEIGHT // 2:
                q_2 += 1
            elif pos_x < self.WIDTH // 2 and pos_y > self.HEIGHT // 2:
                q_3 += 1
            elif pos_x > self.WIDTH // 2 and pos_y > self.HEIGHT // 2:
                q_4 += 1

        return q_1 * q_2 * q_3 * q_4

################################################################################

    def print_hall(self) -> None:
        """
        Print the hall with robots in their positions to reveal the Christmas
        tree Easter egg.
        """

        hall = list([0] * self.WIDTH for _ in range(self.HEIGHT))
        for robot in self._robots:
            hall[robot.pos_y][robot.pos_x] += 1
        print("\n".join("".join(map(str, row)).replace("0", ".")
                        for row in hall))

################################################################################
