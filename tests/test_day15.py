from solutions.day15 import Solution


def test_day15_part1():
    starting_values = [65, 8921]

    # It takes a while to run through all 40M pairs, so just make sure that the
    # first expected match for this test case is detected.
    assert Solution.part1(starting_values, pairs=2) == 0
    assert Solution.part1(starting_values, pairs=3) == 1


def test_day15_part2():
    starting_values = [65, 8921]

    assert Solution.part2(starting_values, pairs=1055) == 0
    assert Solution.part2(starting_values, pairs=1056) == 1
