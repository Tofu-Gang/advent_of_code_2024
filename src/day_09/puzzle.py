__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import List

"""

"""

INPUT_FILE_PATH = "src/day_09/input.txt"
# INPUT_FILE_PATH = "src/day_09/input_test.txt"


################################################################################

def _load_disk_map() -> List[str]:
    """

    :return:
    """

    with open(INPUT_FILE_PATH, "r") as f:
        return list(f.read().strip())


################################################################################

def _get_blocks(disk_map: List[str]) -> List[str]:
    """

    :param disk_map:
    :return:
    """

    blocks = []
    file_id = 0

    for i in range(len(disk_map)):
        if i % 2 == 0:
            # file
            [blocks.append(f"{file_id}") for _ in range(int(disk_map[i]))]
            file_id += 1
        else:
            # free space
            [blocks.append(".") for _ in range(int(disk_map[i]))]
    return blocks


################################################################################

def _defragment_blocks(blocks: List[str]) -> List[str]:
    """

    :param blocks:
    :return:
    """

    for i in reversed(range(len(blocks))):
        block = blocks[i]

        if block == ".":
            continue
        else:
            first_free_space_index = blocks.index(".")

            if first_free_space_index < i:
                blocks[first_free_space_index] = block
                blocks[i] = "."
            else:
                break
    return blocks


################################################################################

def _filesystem_checksum(blocks: List[str]) -> int:
    """

    :param blocks:
    :return:
    """

    return sum(i * int(blocks[i]) for i in range(blocks.index(".")))


################################################################################

def puzzle_01() -> int:
    """
    :return:
    """

    disk_map = _load_disk_map()
    blocks = _get_blocks(disk_map)
    blocks = _defragment_blocks(blocks)
    return _filesystem_checksum(blocks)


################################################################################

def puzzle_02() -> int:
    """
    :return:
    """

    return -1

################################################################################
