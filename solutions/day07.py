"""
Day 6: Memory Reallocation
"""
import re
from collections import Counter
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 7

    @staticmethod
    def process_input(input_raw):
        regex = re.compile(
            r'^(?P<name>\w+) [(](?P<weight>\d+)[)]( -> (?P<children>.*))?$')

        programs = []

        for program in (line.strip() for line in input_raw.split('\n')):
            print(program)
            match = regex.search(program)

            name = match.group('name')
            weight = int(match.group('weight'))
            children = []
            if match.group('children'):
                for child in match.group('children').split(', '):
                    children.append(child)

            programs.append((name, weight, children))

        return programs

    @staticmethod
    def part1(programs):
        programs_with_parents = set(prog[0] for prog in programs)

        for program in programs:
            for child in program[2]:
                programs_with_parents.discard(child)

        return programs_with_parents.pop()

    @staticmethod
    def part2(programs):
        pass


if __name__ == '__main__':
    Solution.main()
