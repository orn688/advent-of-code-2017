"""
Day 6: Memory Reallocation
"""
DAY = 6


def main():
    from utils import get_input_for_day

    banks = [int(blocks) for blocks in get_input_for_day(DAY).split()]

    print(f'Part 1: {part1(banks.copy())}')
    print(f'Part 2: {part2(banks.copy())}')


def part1(banks):
    """
    Determine how many redistributions of memory blocks in the banks it will
    take before we see the same allocation twice. Each redistribution takes
    the first bank with a maximal number of blocks and redistributes them as
    equally as possible over all the blocks, starting at the next index.
    """
    _, seen = find_loop(banks)
    return len(seen)


def part2(banks):
    """
    Find the number of redistributions in the loop; i.e., between the first
    and the second time we see the repeated memory allocation.
    """
    loop_start, seen = find_loop(banks)
    return len(seen) - seen[loop_start]


def find_loop(banks):
    redistributions = 0
    seen = dict()

    while tuple(banks) not in seen:
        seen[tuple(banks)] = redistributions

        max_blocks = max(banks)
        max_index = banks.index(max_blocks)
        banks[max_index] = 0

        start_index = max_index + 1

        for i in range(len(banks)):
            index = (start_index + i) % len(banks)
            banks[index] += max_blocks // len(banks)

        for i in range(max_blocks % len(banks)):
            index = (start_index + i) % len(banks)
            banks[index] += 1

        redistributions += 1

    return tuple(banks), seen


if __name__ == '__main__':
    main()
