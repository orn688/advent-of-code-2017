"""
Day 18: Duet
"""
from collections import defaultdict
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 18

    @staticmethod
    def process_input(input_raw):
        return [instruction.split() for instruction in input_raw.split('\n')]

    @staticmethod
    def part1(instructions):
        registers = defaultdict(lambda: 0)
        last_frequency = None

        i = 0
        while i >= 0 and i < len(instructions):
            operation, op_register, *op_args = instructions[i]
            if op_args:
                if op_args[0].isdigit():
                    op_value = int(op_args[0])
                else:
                    op_value = registers[op_args[0]]
            else:
                op_value = None

            if operation == 'rcv':
                if registers[op_register] != 0:
                    return last_frequency
            elif operation == 'snd':
                last_frequency = registers[op_register]
            elif operation == 'set':
                registers[op_register] = op_value
            elif operation == 'add':
                registers[op_register] += op_value
            elif operation == 'mul':
                registers[op_register] *= op_value
            elif operation == 'mod':
                registers[op_register] %= op_value

            if operation == 'jgz' and registers[op_register] > 0:
                i += op_value
            else:
                i += 1

        return None

    @staticmethod
    def part2(instructions):
        return 0


if __name__ == '__main__':
    Solution.main()
