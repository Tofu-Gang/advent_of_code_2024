__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""
--- Day 3: Mull It Over ---

"Our computers are having issues, so I have no idea if we have any Chief 
Historians in stock! You're welcome to check the warehouse, though," says the 
mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The 
Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are 
having issues again?"
"""

from re import compile
from functools import reduce

INPUT_FILE_PATH = "src/day_03/input.txt"
DIGITS_MIN = 1
DIGITS_MAX = 3
DIGIT_PATTERN = fr"\d{{{DIGITS_MIN},{DIGITS_MAX}}}"
MUL_INSTRUCTION = "mul"
MUL_PATTERN = fr"{MUL_INSTRUCTION}\({DIGIT_PATTERN},{DIGIT_PATTERN}\)"
DO_INSTRUCTION = "do()"
DO_PATTERN = fr"do\(\)"
DONT_INSTRUCTION = "don't()"
DONT_PATTERN = fr"don't\(\)"


################################################################################

def _get_mul_instructions() -> tuple[str, ...]:
    """
    :return: valid mul instructions
    """

    with open(INPUT_FILE_PATH, "r") as f:
        memory = f.read()
        return tuple(compile(MUL_PATTERN).findall(memory))


################################################################################

def _get_all_instructions() -> tuple[str, ...]:
    """
    :return: valid mul, do and don't instructions
    """

    with open(INPUT_FILE_PATH, "r") as f:
        memory = f.read()
        return tuple(
            compile(fr"{MUL_PATTERN}|{DO_PATTERN}|{DONT_PATTERN}")
            .findall(memory))


################################################################################

def _process_mul_instruction(instruction: str) -> int:
    """
    :param instruction: mul instruction
    :return: product of the two number parameters of the mul instruction
    """

    numbers = list(map(int, compile(r"\d+").findall(instruction)))
    return reduce((lambda x, y: x * y), numbers)


################################################################################

def puzzle_01() -> int:
    """
    The computer appears to be trying to run a program, but its memory (your
    puzzle input) is corrupted. All of the instructions have been jumbled up!

    It seems like the goal of the program is just to multiply some numbers. It
    does that with instructions like mul(X,Y), where X and Y are each 1-3 digit
    numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of
    2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like part
    of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or
    mul ( 2 , 4 ) do nothing.

    For example, consider the following section of corrupted memory:
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

    Only the four highlighted sections are real mul instructions. Adding up the
    result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

    :return: Scan the corrupted memory for uncorrupted mul instructions. What do
    you get if you add up all of the results of the multiplications?
    """

    return sum(_process_mul_instruction(instruction)
               for instruction in _get_mul_instructions())


################################################################################

def puzzle_02() -> int:
    """
    As you scan through the corrupted memory, you notice that some of the
    conditional statements are also still intact. If you handle some of the
    uncorrupted conditional statements in the program, you might be able to get
    an even more accurate result.

    There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.
    Only the most recent do() or don't() instruction applies. At the beginning
    of the program, mul instructions are enabled.

    For example:
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

    This corrupted memory is similar to the example from before, but this time
    the mul(5,5) and mul(11,8) instructions are disabled because there is a
    don't() instruction before them. The other mul instructions function
    normally, including the one at the end that gets re-enabled by a do()
    instruction.

    This time, the sum of the results is 48 (2*4 + 8*5).

    :return: Handle the new instructions; what do you get if you add up all of
    the results of just the enabled multiplications?
    """

    enabled = True
    result = 0
    instructions = _get_all_instructions()

    for instruction in instructions:
        if instruction == DO_INSTRUCTION:
            # enable processing mul instructions
            enabled = True
        elif instruction == DONT_INSTRUCTION:
            # disable processing mul instructions
            enabled = False
        else:
            if enabled:
                result += _process_mul_instruction(instruction)
    return result

################################################################################