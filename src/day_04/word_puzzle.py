from typing import List


class WordPuzzle:
    INPUT_FILE_PATH = "src/day_04/input.txt"
    # puzzle 1
    WORD = "XMAS"
    WORD_REVERSED = "SAMX"
    # puzzle 2
    X_WORD = "MAS"
    X_WORD_REVERSED = "SAM"

################################################################################

    def __init__(self):
        """
        Load the word search puzzle from the input file. Extract all positive
        (like forward slash, /) and negative (like backward slash, \) diagonals
        and vertical lines. Mark the height and width of the original puzzle
        form, it is used a lot.
        """

        with open(self.INPUT_FILE_PATH, "r") as f:
            self._original_lines = f.readlines()
            self._width = len(self._original_lines[0])
            self._height = len(self._original_lines)
            self._positive_diagonals = self._get_positive_diagonals()
            self._negative_diagonals = self._get_negative_diagonals()
            self._vertical_lines = self._get_vertical_lines()

################################################################################

    def word_search(self) -> int:
        """
        Look for the puzzle 1 word (including its reversed form) in all
        horizontal and vertical lines and positive and negative diagonals.

        :return: how many times the puzzle 1 word appears in the puzzle
        """

        lines_combined = (self._original_lines +
                          self._positive_diagonals +
                          self._negative_diagonals +
                          self._vertical_lines)
        return sum(line.count(self.WORD) + line.count(self.WORD_REVERSED)
                   for line in lines_combined)

################################################################################

    def x_word_search(self) -> int:
        """
        Look for the puzzle 2 two words forming an x-shape. Use only original
        form of the puzzle (no diagonals nor vertical lines).

        :return: how many times the puzzle 2 x-shape appears in the puzzle
        """

        return sum(
            1
            for row in range(self._height - 2)
            for column in range(self._width - 2)
            if self._is_x_mas(row, column))

################################################################################

    def _get_positive_diagonals(self) -> List[str]:
        """
        :return: All positive diagonals from the puzzle.
        """

        # start in the top left corner; go down the first column and collect
        # each positive diagonal starting in the first column
        return \
            (list("".join(
                self._original_lines[row][row_start - row]
                for row in reversed(range(row_start + 1))
                if row_start - row < self._width)
                  for row_start in range(self._height)) +
             # continue along the last row, start on the second column; go
             # right and collect each positive diagonal starting in the last
             # row
             list("".join(
                self._original_lines[row][self._height - 1 - row + column_start]
                for row in reversed(range(self._height))
                if self._height - 1 - row + column_start < self._width)
                  for column_start in range(1, self._width)))

################################################################################

    def _get_negative_diagonals(self) -> List[str]:
        """
        :return: All negative diagonals from the puzzle.
        """

        # start in the bottom left corner; go up the first column and collect
        # each negative diagonal starting in the first column
        return \
            (list("".join(
                self._original_lines[row][row - row_start]
                for row in range(row_start, self._height)
                if row - row_start < self._width)
                  for row_start in reversed(range(self._height))) +
             # continue along the first row, start on the second column; go
             # right and collect each negative diagonal starting in the first
             # row
             list("".join(
                 self._original_lines[row][column_start + row]
                 for row in range(self._height)
                 if column_start + row < self._width)
                  for column_start in range(1, self._width)))

################################################################################

    def _get_vertical_lines(self) -> List[str]:
        """
        :return: All vertical lines from the puzzle.
        """

        return list(
            "".join(self._original_lines[row][column]
                    for row in range(self._height))
            for column in range(self._width))

################################################################################

    def _is_x_mas(self, row: int, column: int) -> bool:
        """
        :param row: row of the top left edge of the x-shape
        :param column: column of the top left edge of the x-shape
        :return: True if there is the x-shape found in this position, False
        otherwise
        """

        # the \ part of the x-shape
        leg_1 = (self._original_lines[row][column] +
                 self._original_lines[row + 1][column + 1] +
                 self._original_lines[row + 2][column + 2])
        # the / part of the x-shape
        leg_2 = (self._original_lines[row][column + 2] +
                 self._original_lines[row + 1][column + 1] +
                 self._original_lines[row + 2][column])
        x_words = (self.X_WORD, self.X_WORD_REVERSED)
        # both parts of the x-shape must be the puzzle 2 word or its reversed
        # form
        return (leg_1 in x_words) and (leg_2 in x_words)


################################################################################
