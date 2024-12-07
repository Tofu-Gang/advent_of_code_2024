__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from itertools import product

INPUT_FILE_PATH = "src/day_07/input.txt"
# INPUT_FILE_PATH = "src/day_07/input_test.txt"


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        calibrations = tuple(
            {"TEST_VALUE": int(line.split(":")[0].strip()),
             "OPERANDS": list(
                 int(number.strip())
                 for number in line.split(":")[1].strip().split())}
            for line in f.readlines())
        operators = "+*"
        total_calibration_result = 0

        for calibration in calibrations:
            test_value = calibration["TEST_VALUE"]
            operands = calibration["OPERANDS"].copy()
            operators_combinations = list(
                list(combination)
                for combination in product(operators, repeat=len(operands) - 1))

            for i in range(len(tuple(operators_combinations))):
                combination = list(operators_combinations[i])
                equation = f"{operands.pop(0)}"

                while len(combination) > 0 and len(operands) > 0:
                    equation = f"({equation}{combination.pop(0)}{operands.pop(0)})"
                result = eval(equation)
                operands = calibration["OPERANDS"].copy()

                if result == test_value:
                    total_calibration_result += test_value
                    break

        return total_calibration_result


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    return -1

################################################################################
