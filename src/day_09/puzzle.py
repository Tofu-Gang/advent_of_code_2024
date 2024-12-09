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

def _defragment_files(blocks: List[str]) -> List[str]:
    """
    
    :param blocks: 
    :return: 
    """

    for i in reversed(range(len(blocks))):
        block = blocks[i]

        if block == ".":
            continue
        else:
            file_id = blocks[i]
            file_size = _file_size(i, blocks)
            # print(f"FILE_ID: {file_id} FILE_SIZE: {file_size}")
            free_space_index = blocks.index(".")
            free_space_size = _free_space_size(free_space_index, blocks)

            if free_space_index < i:
                while free_space_size < file_size:
                    free_space_index = blocks.index(".", free_space_index + free_space_size)
                    free_space_size = _free_space_size(free_space_index, blocks)

                    if free_space_index > i:
                        free_space_index = None
                        free_space_size = None
                        break
                # print(f"FREE_SPACE_INDEX: {free_space_index} FREE_SPACE_SIZE: {free_space_size}")

                if free_space_index is not None and free_space_size is not None:
                    for j in range(free_space_index, free_space_index + file_size):
                        blocks[j] = file_id
                    for j in range(i - file_size + 1, i + 1):
                        blocks[j] = "."
                # print("".join(blocks))
            else:
                break

    return blocks


################################################################################

def _free_space_size(start_index: int, blocks: List[str]) -> int:
    """

    :param start_index:
    :return:
    """

    if blocks[start_index] == ".":
        free_space_size = 1
        i = start_index + 1
        while i < len(blocks) and blocks[i] == ".":
            i += 1
            free_space_size += 1

        i = start_index - 1
        while i >= 0 and blocks[i] == ".":
            free_space_size += 1
            i -= 1

        return free_space_size
    else:
        return 0


################################################################################

def _file_size(start_index: int, blocks: List[str]) -> int:
    """

    :param start_index:
    :param blocks:
    :return:
    """

    if blocks[start_index].isnumeric():
        file_id = blocks[start_index]
        file_size = 1
        i = start_index + 1
        while i < len(blocks) and blocks[i] == file_id:
            i += 1
            file_size += 1

        i = start_index - 1
        while i >= 0 and blocks[i] == file_id:
            file_size += 1
            i -= 1

        return file_size
    else:
        return 0


################################################################################

def _filesystem_checksum(blocks: List[str]) -> int:
    """

    :param blocks:
    :return:
    """

    return sum(i * int(blocks[i])
               for i in range(len(blocks))
               if blocks[i].isnumeric())


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

    disk_map = _load_disk_map()
    blocks = _get_blocks(disk_map)
    # print("".join(blocks))
    blocks = _defragment_files(blocks)
    return _filesystem_checksum(blocks)

################################################################################
