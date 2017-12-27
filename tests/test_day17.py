from solutions.day17 import Solution


def test_day17_part1():
    assert Solution.part1(3) == 638


def test_day17_part2():
    assert Solution.part2(3, last_value=8) == 5
    assert Solution.part2(3, last_value=9) == 9
