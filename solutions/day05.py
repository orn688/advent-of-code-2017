"""
Day 5: A Maze of Twisty Trampolines, All Alike
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 5

    @staticmethod
    def process_input(input_raw):
        return [int(jump) for jump in input_raw.split()]

    @staticmethod
    def part1(jumps):
        """
        Determine the number of steps it takes to exit the 'maze', by
        starting at index 0 and jumping forward by the number indicated,
        incrementing each value seen.
        """
        curr = 0
        steps = 0
        while curr >= 0 and curr < len(jumps):
            offset = jumps[curr]
            jumps[curr] += 1
            curr += offset
            steps += 1
        return steps

    @staticmethod
    def part2(jumps):
        """
        Determine the number of steps it takes to exit the 'maze', by
        starting at index 0 and jumping forward by the number indicated,
        incrementing each value seen if that value is less than 3, and
        decrementing it otherwise.
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
    Solution.main()
