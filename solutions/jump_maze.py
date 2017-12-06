"""
Day 5: A Maze of Twisty Trampolines, All Alike
"""
DAY = 5


def main():
    from utils import get_input_for_day

    raw_jumps = [int(jump) for jump in get_input_for_day(DAY).split()]

    print(f'Part 1: {part1(raw_jumps)}')
    print(f'Part 2: {part2(raw_jumps)}')


def part1(jumps):
    """
    Determine the number of steps it takes to exit the 'maze', by starting at
    index 0 and jumping forward by the number indicated, incrementing each
    value seen.
    """
    curr = 0
    steps = 0
    while curr >= 0 and curr < len(jumps):
        offset = jumps[curr]
        jumps[curr] += 1
        curr += offset
        steps += 1
    return steps


def part2(jumps):
    """
    Determine the number of steps it takes to exit the 'maze', by starting at
    index 0 and jumping forward by the number indicated, incrementing each
    value seen if that value is less than 3, and decrementing it otherwise.
    """
    curr = 0
    steps = 0
    while curr >= 0 and curr < len(jumps):
        offset = jumps[curr]
        if offset >= 3:
            jumps[curr] -= 1
        else:
            jumps[curr] += 1
        curr += offset
        steps += 1
    return steps


if __name__ == '__main__':
    main()
