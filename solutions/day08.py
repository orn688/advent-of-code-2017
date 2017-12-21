"""
Day 8: I Heard You Like Registers
"""
from collections import defaultdict
from ast import literal_eval
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 8

    @staticmethod
    def process_input(input_raw):
        return [line.strip() for line in input_raw.split('\n') if line.strip()]

    @staticmethod
    def part1(instructions):
        registers = defaultdict(lambda: 0)

        for instruction in instructions:
            (register,
             op_string,
             val,
             _,
             comparison_register,
             comparison) = instruction.split(maxsplit=5)

            condition = str(registers[comparison_register]) + ' ' + comparison

            if eval(condition):
                coeff = 1 if op_string == 'inc' else -1
                registers[register] += (coeff * int(val))

        return max(registers.values())

    @staticmethod
    def part2(instructions):
        registers = defaultdict(lambda: 0)

        all_time_max = 0

        for instruction in instructions:
            (register,
             op_string,
             val,
             _,
             comparison_register,
             comparison) = instruction.split(maxsplit=5)

            condition = str(registers[comparison_register]) + ' ' + comparison

            if eval(condition):
                coeff = 1 if op_string == 'inc' else -1
                registers[register] += (coeff * int(val))

            all_time_max = max(all_time_max, registers[register])

        return all_time_max


if __name__ == '__main__':
    Solution.main()
