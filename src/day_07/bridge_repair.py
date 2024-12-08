__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from itertools import product
from typing import List
from re import compile


class BridgeRepair:
    INPUT_FILE_PATH = "src/day_07/input.txt"
    # INPUT_FILE_PATH = "src/day_07/input_test.txt"
    KEY_TEST_VALUE = "TEST_VALUE"
    KEY_OPERANDS = "OPERANDS"
    CALIBRATION_DELIMITER = ":"
    CONCAT_OPERATOR = "|"
    PATTERN = compile(r"(\([^\(]*?\))")

################################################################################

    def __init__(self):
        """

        """

        self._calibrations = None
        self._operators_1 = "+*"
        self._operators_2 = f"+*{self.CONCAT_OPERATOR}"
        self._load_calibrations()

################################################################################

    @property
    def operators_1(self) -> str:
        """

        :return:
        """

        return self._operators_1

################################################################################

    @property
    def operators_2(self) -> str:
        """

        :return:
        """

        return self._operators_2

################################################################################

    def total_calibration_result_1(self) -> int:
        """

        :return:
        """

        total_calibration_result = 0

        for i in range(len(self._calibrations)):
            calibration = self._calibrations[i]
            test_value = calibration[self.KEY_TEST_VALUE]
            operands = calibration[self.KEY_OPERANDS]
            operators_combinations = list(
                list(combination)
                for combination in product(self._operators_1, repeat=len(operands) - 1))

            for j in range(len(tuple(operators_combinations))):
                print(f"calibration {i}/{len(self._calibrations)} combination {j}/{len(tuple(operators_combinations))}")
                combination = tuple(operators_combinations)[j]

                if self._is_equation_true(operands, combination, test_value):
                    total_calibration_result += test_value
                    break

        return total_calibration_result

################################################################################

    def total_calibration_result_2(self) -> int:
        """

        :return:
        """

        total_calibration_result = 0

        for i in range(len(self._calibrations)):
            calibration = self._calibrations[i]
            test_value = calibration[self.KEY_TEST_VALUE]
            operands = calibration[self.KEY_OPERANDS]
            operators_combinations = list(
                list(combination)
                for combination in product(self._operators_1, repeat=len(operands) - 1))

            for j in range(len(tuple(operators_combinations))):
                print(f"calibration {i}/{len(self._calibrations)} combination {j}/{len(tuple(operators_combinations))}")
                combination = tuple(operators_combinations)[j]

                if self._is_equation_true(operands, combination, test_value):
                    total_calibration_result += test_value
                    break
            else:
                operators_combinations = list(
                    list(combination)
                    for combination in
                    product(self._operators_2, repeat=len(operands) - 1))
                for j in range(len(tuple(operators_combinations))):
                    print(f"calibration {i}/{len(self._calibrations)} combination {j}/{len(tuple(operators_combinations))}")
                    combination = tuple(operators_combinations)[j]

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
        operators = operators.copy()
        equation = f"{operands.pop(0)}"

        while len(operands) > 0 and len(operators) > 0:
            equation = f"({equation}{operators.pop(0)}{operands.pop(0)})"

        result = -1
        while True:
            try:
                segment = self.PATTERN.findall(equation)[0]
                if self.CONCAT_OPERATOR in segment:
                    result = eval("".join(map(lambda element: element.strip(), segment.split(self.CONCAT_OPERATOR))))
                else:
                    result = eval(segment)

                if result > test_value:
                    return False
                else:
                    equation = equation.replace(segment, str(result))
            except IndexError:
                return result == test_value

################################################################################
