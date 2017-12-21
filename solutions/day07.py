"""
Day 7: Recursive Circus
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
        """Determine the bottom (root) program."""
        programs_with_parents = set(prog[0] for prog in programs)

        for program in programs:
            for child in program[2]:
                programs_with_parents.discard(child)

        # Assumes only one program is left in the set (i.e., doesn't have
        # parent programs).
        return programs_with_parents.pop()

    @staticmethod
    def part2(programs):
        """Determine the program that causes an imbalance in the tower."""
        program_weights = {p[0]: p[1] for p in programs}
        children = {p[0]: p[2] for p in programs}

        root = Solution.part1(programs)
        total_weights = Solution._calculate_total_weights(root,
                                                          program_weights,
                                                          children)

        found_imbalance = False
        stack = [root]
        curr = None
        weight_diff = 0

        while True:
            if found_imbalance:
                # We are already on the branch of the stack that has an
                # imbalance; determine if the imbalance occurs here or further
                # down the stack.
                if Solution._weights_are_equal(total_weights, children[curr]):
                    # If the current program's children are all of equal total
                    # weight, then it must be the current program itself that
                    # is causing the imbalance.
                    return program_weights[curr] - weight_diff
                else:
                    # Otherwise, continue down along the path of children with
                    # imbalances.
                    curr = Solution._unique_weight_program(total_weights,
                                                           children[curr])
            else:
                curr = stack.pop()
                # Check if the imbalance starts here.
                if Solution._weights_are_equal(total_weights, children[curr]):
                    # If not, just move on to the current node's children.
                    stack += children[curr]
                else:
                    # Determine the difference in the imbalance.
                    found_imbalance = True
                    duplicate_weight = Solution._duplicate_weight(
                        total_weights, children[curr])
                    unique_weight_program = Solution._unique_weight_program(
                        total_weights, children[curr])
                    unique_weight = total_weights[unique_weight_program]
                    weight_diff = unique_weight - duplicate_weight

                    curr = unique_weight_program

        return 0

    @staticmethod
    def _calculate_total_weights(root, weights, children, total_weights=None):
        if total_weights is None:
            total_weights = dict()

        for child in children[root]:
            Solution._calculate_total_weights(child, weights, children,
                                              total_weights)
        total_weights[root] = (weights[root] +
                               sum(total_weights[c] for c in children[root]))

        return total_weights

    @staticmethod
    def _weights_are_equal(all_weights, programs):
        weights = [all_weights[p] for p in programs]
        return len(set(weights)) <= 1

    @staticmethod
    def _unique_weight_program(all_weights, programs):
        weights = [all_weights[p] for p in programs]
        weight_counter = Counter(weights)

        for weight, count in weight_counter.items():
            if count == 1:
                return [p for p in programs if all_weights[p] == weight][0]

        return None

    @staticmethod
    def _duplicate_weight(all_weights, programs):
        weights = [all_weights[p] for p in programs]
        weight_counter = Counter(weights)

        for weight, count in weight_counter.items():
            if count > 1:
                return weight

        return None


if __name__ == '__main__':
    Solution.main()
