__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

"""

"""

from typing import Tuple

INPUT_FILE_PATH = "src/day_05/input.txt"


################################################################################

def _load_rules() -> Tuple[Tuple[int, ...], ...]:
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        return tuple(tuple(map(int, line.split("|")))
                     for line in lines if "|" in line)


################################################################################

def _load_updates() -> Tuple[Tuple[int, ...], ...]:
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        lines = f.readlines()
        return tuple((tuple(map(int, line.split(",")))
                      for line in lines if "," in line))


################################################################################

def _get_middle_page(update: Tuple[int, ...]) -> int:
    """

    :param update:
    :return:
    """

    return update[int(len(update) / 2)]


################################################################################

def _update_follows_rule(update: Tuple[int, ...], rule: Tuple[int, ...]) -> bool:
    """

    :param update:
    :param rule:
    :return:
    """

    return (rule[0] not in update or rule[1] not in update or
            update.index(rule[0]) < update.index(rule[1]))


################################################################################

def _fix_update_to_rule(update: Tuple[int, ...], rule: Tuple[int, ...]) -> Tuple[int, ...]:
    """

    :param update:
    :param rule:
    :return:
    """

    if rule[0] in update and rule[1] in update:
        index_0 = update.index(rule[0])
        index_1 = update.index(rule[1])

        if index_0 < index_1:
            return update
        else:
            result = list(update)
            result[index_0] = rule[1]
            result[index_1] = rule[0]
            return tuple(result)
    else:
        return update


################################################################################

def _fix_update(update: Tuple[int, ...], rules: Tuple[Tuple[int, ...], ...]) -> Tuple[int, ...]:
    """

    :param update:
    :param rules:
    :return:
    """

    while not all(_update_follows_rule(update, rule) for rule in rules):
        for rule in rules:
            update = _fix_update_to_rule(update, rule)
    return update


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    rules = _load_rules()
    updates = _load_updates()
    return sum(_get_middle_page(update) for update in updates
               if all(_update_follows_rule(update, rule) for rule in rules))


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    rules = _load_rules()
    updates = _load_updates()
    return sum(_get_middle_page(_fix_update(update, rules))
               for update in updates
               if not all(_update_follows_rule(update, rule) for rule in rules))

################################################################################
