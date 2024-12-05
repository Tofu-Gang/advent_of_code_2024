from typing import List


class WordPuzzle:
    INPUT_FILE_PATH = "src/day_04/input.txt"
    WORD = "XMAS"
    WORD_REVERSED = "SAMX"
    X_WORD = "MAS"
    X_WORD_REVERSED = "SAM"

################################################################################

    def __init__(self):
        """

        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._original_lines = f.readlines()
            self._positive_diagonals = self._get_positive_diagonals()
            self._negative_diagonals = self._get_negative_diagonals()
            self._vertical_lines = self._get_vertical_lines()

################################################################################

    @property
    def word_search(self) -> int:
        """

        :return:
        """

        lines_combined = (self._original_lines +
                          self._positive_diagonals +
                          self._negative_diagonals +
                          self._vertical_lines)
        return sum(line.count(self.WORD) + line.count(self.WORD_REVERSED)
                   for line in lines_combined)

################################################################################

    def _get_positive_diagonals(self) -> List[str]:
        """

        :return:
        """

        diagonals = list(
            "".join(self._original_lines[row][row_start - row]
                    for row in reversed(range(row_start + 1))
                    if row_start - row < len(self._original_lines[0]))
            for row_start in range(len(self._original_lines)))

        row_start = len(self._original_lines) - 1
        for column_start in range(1, len(self._original_lines[0])):
            line = ""
            for row in reversed(range(row_start + 1)):
                column = row_start - row + column_start
                if column < len(self._original_lines[0]):
                    line += self._original_lines[row][column]
                else:
                    break
            diagonals.append(line)

        return diagonals

################################################################################

    def _get_negative_diagonals(self) -> List[str]:
        """

        :return:
        """

        diagonals = []

        for row_start in reversed(range(len(self._original_lines))):
            line = ""
            for row in range(row_start, len(self._original_lines)):
                column = row - row_start
                if column < len(self._original_lines[0]):
                    line += self._original_lines[row][column]
                else:
                    break
            diagonals.append(line)

        for column_start in range(1, len(self._original_lines[0])):
            line = ""
            for row in range(len(self._original_lines)):
                column = column_start + row
                if column < len(self._original_lines[0]):
                    line += self._original_lines[row][column]
                else:
                    break
            diagonals.append(line)

        return diagonals

################################################################################

    def _get_vertical_lines(self) -> List[str]:
        """

        :return:
        """

        vertical_lines = []

        for column in range(len(self._original_lines[0])):
            line = ""
            for row in range(len(self._original_lines)):
                line += self._original_lines[row][column]
            vertical_lines.append(line)

        return vertical_lines

################################################################################
