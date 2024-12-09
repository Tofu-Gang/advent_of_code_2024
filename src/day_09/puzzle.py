__author__ = "Jakub Franěk"
__email__ = "tofugangsw@gmail.com"

from typing import List

"""
--- Day 9: Disk Fragmenter ---

Another push of the button leaves you in the familiar hallways of some friendly 
amphipods! Good thing you each somehow got your own personal mini submarine. The 
Historians jet away in search of the Chief, mostly by driving directly into 
walls.

While The Historians quickly figure out how to pilot these things, you notice an 
amphipod in the corner struggling with his computer. He's trying to make more 
contiguous free space by compacting all of the files, but his program isn't 
working; you offer to help.
"""

INPUT_FILE_PATH = "src/day_09/input.txt"
FREE_SPACE = "."


################################################################################

def _load_disk_map() -> List[str]:
    """
    :return: Disk map from the input file.
    """

    with open(INPUT_FILE_PATH, "r") as f:
        return list(f.read().strip())


################################################################################

def _get_blocks(disk_map: List[str]) -> List[str]:
    """
    :param disk_map: disk map from the input file
    :return: list of disk blocks, each containing either free space or file ID
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
            [blocks.append(FREE_SPACE) for _ in range(int(disk_map[i]))]
    return blocks


################################################################################

def _defragment_blocks(blocks: List[str]) -> List[str]:
    """
    :param blocks: list of disk blocks, each containing either free space or
    file ID
    :return: defragmented list of blocks
    """

    for i in reversed(range(len(blocks))):
        # start at the end of the list, move back
        block = blocks[i]

        if block.isnumeric():
            # this block contains a file ID
            file_id = blocks[i]
            # find the first free empty space from the start of the blocks list
            first_free_space_index = blocks.index(FREE_SPACE)

            if first_free_space_index < i:
                # swap the file block and the free space
                blocks[first_free_space_index] = file_id
                blocks[i] = FREE_SPACE
            else:
                # move file blocks only to the left, closer to the start of the
                # list; if there is no free space to the left from the file
                # block, stop the defragmentation process
                break
    return blocks


################################################################################

def _defragment_files(blocks: List[str]) -> List[str]:
    """
    :param blocks: list of disk blocks, each containing either free space or
    file ID
    :return: defragmented list of blocks
    """

    for i in reversed(range(len(blocks))):
        # start at the end of the list, move back
        block = blocks[i]

        if block.isnumeric():
            # this block contains a file ID
            file_id = block
            file_size = _file_size(i, blocks)
            # find the first free empty space from the start of the blocks list
            # that is big enough to hold the whole file
            free_space_index = blocks.index(".")
            free_space_size = _free_space_size(free_space_index, blocks)

            if free_space_index < i:
                while free_space_size < file_size:
                    free_space_index = blocks.index(
                        FREE_SPACE, free_space_index + free_space_size)
                    free_space_size = _free_space_size(free_space_index, blocks)

                    if free_space_index > i:
                        # no free space big enough to the left from the file
                        # block
                        free_space_index = None
                        free_space_size = None
                        break

                if free_space_index is not None and free_space_size is not None:
                    # swap the file blocks and the free space for the whole file
                    blocks[free_space_index:free_space_index + file_size] = (
                            [file_id] * file_size)
                    blocks[i - file_size + 1: i + 1] = [FREE_SPACE] * file_size
            else:
                # move file blocks only to the left, closer to the start of the
                # list; if there is no free space to the left from the file
                # block, stop the defragmentation process
                break

    return blocks


################################################################################

def _free_space_size(start_index: int, blocks: List[str]) -> int:
    """
    :param start_index: block index
    :param blocks: list of disk blocks, each containing either free space or
    file ID
    :return: size of the continuous free space containing the param index or
    zero if there is no free space on that index
    """

    if blocks[start_index] == FREE_SPACE:
        free_space_size = 1
        i = start_index + 1
        while i < len(blocks) and blocks[i] == FREE_SPACE:
            i += 1
            free_space_size += 1

        i = start_index - 1
        while i >= 0 and blocks[i] == FREE_SPACE:
            free_space_size += 1
            i -= 1

        return free_space_size
    else:
        return 0


################################################################################

def _file_size(start_index: int, blocks: List[str]) -> int:
    """
    :param start_index: block index
    :param blocks: list of disk blocks, each containing either free space or
    file ID
    :return: file size containing the block on the param index or zero if there
    is no file on that index
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
    :param blocks: list of disk blocks, each containing either free space or
    file ID
    :return: filesystem checksum
    """

    return sum(i * int(blocks[i])
               for i in range(len(blocks))
               if blocks[i].isnumeric())


################################################################################

def puzzle_01() -> int:
    """
    He shows you the disk map (your puzzle input) he's already generated. For
    example:
    2333133121414131402

    The disk map uses a dense format to represent the layout of files and free
    space on the disk. The digits alternate between indicating the length of a
    file and the length of free space.

    So, a disk map like 12345 would represent a one-block file, two blocks of
    free space, a three-block file, four blocks of free space, and then a five-
    -block file. A disk map like 90909 would represent three nine-block files in
    a row (with no free space between them).

    Each file on disk also has an ID number based on the order of the files as
    they appear before they are rearranged, starting with ID 0. So, the disk map
    12345 has three files: a one-block file with ID 0, a three-block file with
    ID 1, and a five-block file with ID 2. Using one character for each block
    where digits are the file ID and . is free space, the disk map 12345
    represents these individual blocks:
    0..111....22222

    The first example above, 2333133121414131402, represents these individual
    blocks:
    00...111...2...333.44.5555.6666.777.888899

    The amphipod would like to move file blocks one at a time from the end of
    the disk to the leftmost free space block (until there are no gaps remaining
    between file blocks). For the disk map 12345, the process looks like this:
    0..111....22222
    02.111....2222.
    022111....222..
    0221112...22...
    02211122..2....
    022111222......

    The first example requires a few more steps:
    00...111...2...333.44.5555.6666.777.888899
    009..111...2...333.44.5555.6666.777.88889.
    0099.111...2...333.44.5555.6666.777.8888..
    00998111...2...333.44.5555.6666.777.888...
    009981118..2...333.44.5555.6666.777.88....
    0099811188.2...333.44.5555.6666.777.8.....
    009981118882...333.44.5555.6666.777.......
    0099811188827..333.44.5555.6666.77........
    00998111888277.333.44.5555.6666.7.........
    009981118882777333.44.5555.6666...........
    009981118882777333644.5555.666............
    00998111888277733364465555.66.............
    0099811188827773336446555566..............

    The final step of this file-compacting process is to update the filesystem
    checksum. To calculate the checksum, add up the result of multiplying each
    of these blocks' position with the file ID number it contains. The leftmost
    block is in position 0. If a block contains free space, skip it instead.

    Continuing the first example, the first few blocks' position multiplied by
    its file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27,
    4 * 8 = 32, and so on. In this example, the checksum is the sum of these,
    1928.

    :return: Compact the amphipod's hard drive using the process he requested.
    What is the resulting filesystem checksum?
    """

    disk_map = _load_disk_map()
    blocks = _get_blocks(disk_map)
    blocks = _defragment_blocks(blocks)
    return _filesystem_checksum(blocks)


################################################################################

def puzzle_02() -> int:
    """
    Upon completion, two things immediately become clear. First, the disk
    definitely has a lot more contiguous free space, just like the amphipod
    hoped. Second, the computer is running much more slowly! Maybe introducing
    all of that file system fragmentation was a bad idea?

    The eager amphipod already has a new plan: rather than move individual
    blocks, he'd like to try compacting the files on his disk by moving whole
    files instead.

    This time, attempt to move whole files to the leftmost span of free space
    blocks that could fit the file. Attempt to move each file exactly once in
    order of decreasing file ID number starting with the file with the highest
    file ID number. If there is no span of free space to the left of a file that
    is large enough to fit the file, the file does not move.

    The first example from above now proceeds differently:
    00...111...2...333.44.5555.6666.777.888899
    0099.111...2...333.44.5555.6666.777.8888..
    0099.1117772...333.44.5555.6666.....8888..
    0099.111777244.333....5555.6666.....8888..
    00992111777.44.333....5555.6666.....8888..

    The process of updating the filesystem checksum is the same; now, this
    example's checksum would be 2858.

    :return: Start over, now compacting the amphipod's hard drive using this new
    method instead. What is the resulting filesystem checksum?
    """

    disk_map = _load_disk_map()
    blocks = _get_blocks(disk_map)
    blocks = _defragment_files(blocks)
    return _filesystem_checksum(blocks)

################################################################################
