from utils import get_input_for_day


class SolutionBase:
    day = 0

    @classmethod
    def main(cls):
        print(f'Day {cls.day}')

        puzzle_input1 = cls.process_input(get_input_for_day(cls.day))
        print(f'Part 1: {cls.part1(puzzle_input1)}')

        puzzle_input2 = cls.process_input(get_input_for_day(cls.day))
        print(f'Part 2: {cls.part2(puzzle_input2)}')

    @staticmethod
    def process_input(input_raw):
        # Do nothing, by default.
        return input_raw

    @staticmethod
    def part1(puzzle_input):
        raise NotImplementedError()

    @staticmethod
    def part2(puzzle_input):
        raise NotImplementedError()
