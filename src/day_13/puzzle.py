__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from re import compile

INPUT_FILE_PATH = "src/day_13/input.txt"
# INPUT_FILE_PATH = "src/day_13/input_test.txt"
BUTTON_A = "A"
BUTTON_B = "B"
PRIZE = "PRIZE"
RIGHT = "X"
FORWARD = "Y"
BUTTON_PRESS_LIMIT = 100


################################################################################

def _load_machines():
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        pattern = compile(r"\d+")
        machines = []

        for i in range(0, len(lines), 4):
            machine = dict()
            numbers = pattern.findall(lines[i])
            machine[BUTTON_A] = {
                RIGHT: int(numbers[0]),
                FORWARD: int(numbers[1])
            }
            numbers = pattern.findall(lines[i + 1])
            machine[BUTTON_B] = {
                RIGHT: int(numbers[0]),
                FORWARD: int(numbers[1])
            }
            numbers = pattern.findall(lines[i + 2])
            machine[PRIZE] = {
                RIGHT: int(numbers[0]),
                FORWARD: int(numbers[1])
            }
            machines.append(machine)
        return machines


################################################################################

def _play_machine(machine):
    """

    :return:
    """

    if (BUTTON_PRESS_LIMIT * machine[BUTTON_A][FORWARD] +
            BUTTON_PRESS_LIMIT * machine[BUTTON_B][FORWARD] <
            machine[PRIZE][FORWARD] or
            BUTTON_PRESS_LIMIT * machine[BUTTON_A][RIGHT] +
            BUTTON_PRESS_LIMIT * machine[BUTTON_B][RIGHT] <
            machine[PRIZE][RIGHT]):
        return 0
    else:
        for i in range(BUTTON_PRESS_LIMIT):
            for j in range(BUTTON_PRESS_LIMIT):
                if (i * machine[BUTTON_A][FORWARD] +
                        j * machine[BUTTON_B][FORWARD] ==
                        machine[PRIZE][FORWARD] and
                        i * machine[BUTTON_A][RIGHT] +
                        j * machine[BUTTON_B][RIGHT] ==
                        machine[PRIZE][RIGHT]):
                    return i * 3 + j
        return 0


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    machines = _load_machines()
    return sum(_play_machine(machine) for machine in machines)


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    return -1

################################################################################
