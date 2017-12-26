"""
Day 16: Permutation Promenade
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 16

    @staticmethod
    def process_input(input_raw):
        return input_raw.split(',')

    @staticmethod
    def part1(moves, programs=None):
        if not programs:
            programs = [chr(code) for code in range(ord('a'), ord('p') + 1)]

        for move in moves:
            if move.startswith('s'): # Spin
                spin_count = int(move[1:])
                programs = (programs[-spin_count:] +
                            programs[:len(programs) - spin_count])
            elif move.startswith('x'): # Exchange two programs by index.
                i, j = (int(idx) for idx in move[1:].split('/'))
                programs[i], programs[j] = programs[j], programs[i]
            elif move.startswith('p'): # Exchange two programs by name.
                partner1, partner2 = move[1:].split('/')
                i, j = programs.index(partner1), programs.index(partner2)
                programs[i], programs[j] = programs[j], programs[i]

        return ''.join(programs)

    @staticmethod
    def part2(moves, programs=None):
        if not programs:
            programs = [chr(code) for code in range(ord('a'), ord('p') + 1)]

        initial = programs.copy()
        programs_after_1_move = list(Solution.part1(moves, programs))
        programs_after_2_moves = list(Solution.part1(moves,
                                                     programs_after_1_move))

        bijection = [programs_after_2_moves.index(program)
                     for program in initial]

        for _ in range(5):
            programs = [programs[i] for i in bijection]

        reps = 10

        while reps <= 1_000_000_000:
            bijection = [programs.index(program) for program in initial]

            programs = initial
            for _ in range(10):
                programs = [programs[i] for i in bijection]

            reps *= 10

        return ''.join(programs)


if __name__ == '__main__':
    Solution.main()
