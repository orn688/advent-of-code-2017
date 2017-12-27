"""
Day 9: Stream Processing
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 9

    @staticmethod
    def part1(stream):
        total_score = 0
        in_garbage = False
        next_char_cancelled = False
        groups_open = 1

        for char in stream:
            if in_garbage:
                if next_char_cancelled:
                    next_char_cancelled = False
                    continue
                elif char == '!':
                    next_char_cancelled = True
                elif char == '>':
                    in_garbage = False
            else:
                if char == '{':
                    groups_open += 1
                if char == '}':
                    groups_open -= 1
                    total_score += groups_open
                elif char == '<':
                    in_garbage = True

        return total_score

    @staticmethod
    def part2(stream):
        garbage_char_count = 0
        in_garbage = False
        next_char_cancelled = False

        for char in stream:
            if in_garbage:
                if next_char_cancelled:
                    next_char_cancelled = False
                    continue
                elif char == '!':
                    next_char_cancelled = True
                elif char == '>':
                    in_garbage = False
                else:
                    garbage_char_count += 1
            elif char == '<':
                in_garbage = True

        return garbage_char_count


if __name__ == '__main__':
    Solution.main()
