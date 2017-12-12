"""
Day 2: Corruption Checksum
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 2

    @staticmethod
    def process_input(input_raw):
        return [int(num) for num in input_raw.split('\n')]

    @staticmethod
    def part1(spreadsheet):
        """
        Calculate the sum of the differences between the min and the max
        value in each row.
        """
        total = 0
        for row in spreadsheet:
            total += max(row) - min(row)

        return total

    @staticmethod
    def part2(spreadsheet):
        """
        Calculate the sum of the quotients of the only two numbers on each row
        such that one evenly divides the other.
        """
        total = 0
        for row in spreadsheet:
            for i, numerator in enumerate(row):
                for j, denominator in enumerate(row):
                    if i != j and numerator % denominator == 0:
                        total += numerator // denominator
                        break

        return total


if __name__ == '__main__':
    Solution.main()
