from solutions.day08 import Solution


def test_day08_part1():
    test_input = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

    instructions = Solution.process_input(test_input)
    assert Solution.part1(instructions) == 1


def test_day08_part2():
    test_input = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

    instructions = Solution.process_input(test_input)
    assert Solution.part2(instructions) == 10
