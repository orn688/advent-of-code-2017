"""
Day 15: Dueling Generators
"""
from solution_base import SolutionBase


A_FACTOR = 16_807
B_FACTOR = 48_271
DIVISOR = 2_147_483_647


class Solution(SolutionBase):
    day = 15

    @staticmethod
    def process_input(input_raw):
        return [int(line.split()[-1]) for line in input_raw.split('\n')]

    @staticmethod
    def part1(starting_values, pairs=40_000_000):
        a, b = starting_values
        matching_pair_count = 0
        mask = 0xffff

        for _ in range(pairs):
            a = (a * A_FACTOR) % DIVISOR
            b = (b * B_FACTOR) % DIVISOR

            if a & mask == b & mask:
                matching_pair_count += 1

        return matching_pair_count

    @staticmethod
    def part2(starting_values, pairs=5_000_000):
        matching_pair_count = 0
        mask = 0xffff

        gen_a = Solution._gen_a(starting_values[0])
        gen_b = Solution._gen_b(starting_values[1])

        for _ in range(pairs):
            a = next(gen_a)
            b = next(gen_b)

            if a & mask == b & mask:
                matching_pair_count += 1

        return matching_pair_count

    @staticmethod
    def _gen_a(starting_value):
        a = starting_value

        while True:
            a = (a * A_FACTOR) % DIVISOR
            if a % 4 == 0:
                yield a

    @staticmethod
    def _gen_b(starting_value):
        b = starting_value

        while True:
            b = (b * B_FACTOR) % DIVISOR
            if b % 8 == 0:
                yield b


if __name__ == '__main__':
    Solution.main()
