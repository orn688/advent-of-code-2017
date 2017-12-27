"""
Day 17: Spinlock
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 17

    @staticmethod
    def process_input(input_raw):
        return int(input_raw.strip())

    @staticmethod
    def part1(steps):
        buffer = [0]
        position = 0

        for i in range(1, 2018):
            position = (position + steps + 1) % len(buffer)
            buffer.insert(position, i)

        index = buffer.index(2017) + 1
        return buffer[index] if index < len(buffer) else None

    @staticmethod
    def part2(steps, last_value=50_000_000):
        value_after_0 = None
        position = 0

        for i in range(1, last_value + 1):
            buffer_length = i
            position = (position + steps) % buffer_length + 1

            if position == 1:
                value_after_0 = i

        return value_after_0


if __name__ == '__main__':
    Solution.main()
