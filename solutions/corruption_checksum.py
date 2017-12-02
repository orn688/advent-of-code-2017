"""
Day 2: Corruption Checksum
"""


def main():
    from utils import get_input_for_day

    spreadsheet = get_input_for_day(2)

    print(f'Part 1: {part1(spreadsheet)}')
    print(f'Part 2: {part2(spreadsheet)}')


def part1(spreadsheet):
    """
    Calculate the sum of the differences between the min and the max value in
    each row.
    """
    total = 0
    for row in spreadsheet.split('\n'):
        nums = [int(num) for num in row.split()]
        total += max(nums) - min(nums)

    return total


def part2(spreadsheet):
    """
    Calculate the sum of the quotients of the only two numbers on each row
    such that one evenly divides the other.
    """
    total = 0
    for row in spreadsheet.split('\n'):
        nums = [int(num) for num in row.split()]
        for i, numerator in enumerate(nums):
            for j, denominator in enumerate(nums):
                if i != j and numerator % denominator == 0:
                    total += numerator // denominator
                    break

    return total


if __name__ == '__main__':
    main()
