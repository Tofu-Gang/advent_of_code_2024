__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple

"""
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk 
from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no 
sign of the Chief Historian, the engineers there run up to you as soon as they 
see you. Apparently, they still talk about the time Rudolph was saved through 
molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate 
your help analyzing some unusual data from the Red-Nosed reactor. You turn to 
check if The Historians are waiting for you, but they seem to have already 
divided into groups that are currently searching every corner of the facility. 
You offer to help with the unusual data.
"""

INPUT_FILE_PATH = "src/day_02/input.txt"
DELTA_MIN = 1
DELTA_MAX = 3


################################################################################

def _levels_increasing_safely(report: Tuple[int]) -> bool:
    """
    :param report: Red-Nosed reactor report
    :return: True if levels in report are increasing safely, False otherwise
    """

    # safe increase from a level to another has to be between specified min and
    # max values
    return all(DELTA_MIN <= report[i + 1] - report[i] <= DELTA_MAX
               for i in range(len(report) - 1))


################################################################################

def _levels_decreasing_safely(report: Tuple[int]) -> bool:
    """
    :param report: Red-Nosed reactor report
    :return: True if levels in report are decreasing safely, False otherwise
    """

    # safe decrease from a level to another has to be between specified min and
    # max values
    return all(DELTA_MIN <= report[i] - report[i + 1] <= DELTA_MAX
               for i in range(len(report) - 1))


################################################################################

def _is_report_safe(report: Tuple[int]) -> bool:
    """
    :param report: Red-Nosed reactor report
    :return: True if the report is safe, False otherwise
    """

    # report is safe if levels all either increase or decrease safely (reading
    # the report from left to right)
    return (_levels_decreasing_safely(report)
            or _levels_increasing_safely(report))


################################################################################

def _is_report_safe_with_problem_dampener(report: Tuple[int]) -> bool:
    """
    :param report: Red-Nosed reactor report
    :return: True if the report is safe using problem dampener, False otherwise
    """

    # Using problem dampener allows us to remove any one level from the report;
    # this can make an unsafe report safe. Try all possible usages of problem
    # dampener.
    return any(_is_report_safe(tuple(report[0:i] + report[i + 1:]))
               for i in range(len(report)))


################################################################################

def puzzle_01() -> int:
    """
    The unusual data (your puzzle input) consists of many reports, one report
    per line. Each report is a list of numbers called levels that are separated
    by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

    This example data contains six reports each containing five levels.

    The engineers are trying to figure out which reports are safe. The Red-Nosed
    reactor safety systems can only tolerate levels that are either gradually
    increasing or gradually decreasing. So, a report only counts as safe if both
    of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    In the example above, the reports can be found safe or unsafe by checking
    those rules:

    -7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    -1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    -9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    -1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    -8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    -1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

    So, in this example, 2 reports are safe.

    :return: Analyze the unusual data from the engineers. How many reports are
    safe?
    """

    with open(INPUT_FILE_PATH, "r") as f:
        reports = tuple(tuple(map(int, line.split())) for line in f.readlines())
        return len(tuple(filter(_is_report_safe, reports)))


################################################################################

def puzzle_02() -> int:
    """
    The engineers are surprised by the low number of safe reports until they
    realize they forgot to tell you about the Problem Dampener.

    The Problem Dampener is a reactor-mounted module that lets the reactor
    safety systems tolerate a single bad level in what would otherwise be a safe
    report. It's like the bad level never happened!

    Now, the same rules apply as before, except if removing a single level from
    an unsafe report would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:

    -7 6 4 2 1: Safe without removing any level.
    -1 2 7 8 9: Unsafe regardless of which level is removed.
    -9 7 6 2 1: Unsafe regardless of which level is removed.
    -1 3 2 4 5: Safe by removing the second level, 3.
    -8 6 4 4 1: Safe by removing the third level, 4.
    -1 3 6 7 9: Safe without removing any level.

    Thanks to the Problem Dampener, 4 reports are actually safe!

    :return: Update your analysis by handling situations where the Problem
    Dampener can remove a single level from unsafe reports. How many reports are
    now safe?
    """

    with open(INPUT_FILE_PATH, "r") as f:
        reports = tuple(tuple(map(int, line.split())) for line in f.readlines())
        return len(tuple(filter(
            _is_report_safe_with_problem_dampener, reports)))

################################################################################
