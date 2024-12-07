__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from itertools import product
from typing import List


class BridgeRepair:
    INPUT_FILE_PATH = "src/day_07/input.txt"
    # INPUT_FILE_PATH = "src/day_07/input_test.txt"
    KEY_TEST_VALUE = "TEST_VALUE"
    KEY_OPERANDS = "OPERANDS"
    CALIBRATION_DELIMITER = ":"

################################################################################

    def __init__(self):
        """

        """

        self._calibrations = None
        self._operators_1 = "+*"
        self._operators_2 = "+*|"
        self._load_calibrations()

################################################################################

    def total_calibration_result(self) -> int:
        """

        :return:
        """

        total_calibration_result = 0

        for calibration in self._calibrations:
            test_value = calibration[self.KEY_TEST_VALUE]
            operands = calibration[self.KEY_OPERANDS]
            operators_combinations = list(
                list(combination)
                for combination in product(self._operators_1, repeat=len(operands) - 1))

            for combination in tuple(operators_combinations):
                if self._is_equation_true(operands, combination, test_value):
                    total_calibration_result += test_value
                    break

        return total_calibration_result

################################################################################

    def _load_calibrations(self) -> None:
        """

        :return:
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._calibrations = tuple(
                {self.KEY_TEST_VALUE: int(
                    line.split(self.CALIBRATION_DELIMITER)[0].strip()),
                 self.KEY_OPERANDS: list(
                     int(number.strip())
                     for number in line.split(self.CALIBRATION_DELIMITER)[1].strip().split())}
                for line in f.readlines())

################################################################################

    def _is_equation_true(self, operands: List[int], operators: List[str], test_value) -> bool:
        """

        :param operands:
        :param operators:
        :param test_value:
        :return:
        """

        operands = operands.copy()
        equation = f"{operands.pop(0)}"

        while len(operands) > 0 and len(operators) > 0:
            equation = f"({equation}{operators.pop(0)}{operands.pop(0)})"
        result = eval(equation)

        return result == test_value

################################################################################
