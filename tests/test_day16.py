from solutions.day16 import Solution


def test_day16_part1():
    moves = ['s1', 'x3/4', 'pe/b']
    programs = list('abcde')

    assert Solution.part1(moves, programs) == 'baedc'


def test_day16_part2():
    assert False
