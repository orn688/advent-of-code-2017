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

        # Assumes only one program is left in the set (i.e., doesn't have
        # parent programs).
        return programs_with_parents.pop()

    @staticmethod
    def part2(programs):
        program_weights = {p[0]: p[1] for p in programs}
        program_children = {p[0]: p[2] for p in programs}

        weight_sums = dict()

        def calculate_weight_sum(program):
            weight_sum = program_weights[program]
            for child in program_children[program]:
                if child not in weight_sums:
                    weight_sums[child] = calculate_weight_sum(child)
                weight_sum += weight_sums[child]

            return weight_sum

        for program in program_weights:
            if program not in weight_sums:
                weight_sums[program] = calculate_weight_sum(program)

        program = None
        weight_counter = Counter()

        for program in program_weights:
            weight_counter = Counter(program_weights[c]
                                     for c in program_children[program])
            if len(weight_counter) > 1:
                break

        while program:
            unique_weight = [weight
                             for weight, count in weight_counter.items()
                             if count == 1][0]
            duplicate_weight = [w for w, c in weight_counter.items()
                                if c > 1][0]

            difference = duplicate_weight - unique_weight

            unique_child = [child
                            for child in program_children[curr]
                            if program_weights[child] == unique_weight][0]
            grandchildren_weights = [program_weights[c] for c in
                                     program_children[unique_child]]
            if len(set(grandchildren_weights)) > 1:
                prev = curr
                curr = unique_child
            else:
                return duplicate_weights[0] if duplicate_weights


if __name__ == '__main__':
    Solution.main()
