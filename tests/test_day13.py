from solutions.day13 import Solution


def test_day13_part1():
    input_raw = """
0: 3
1: 2
4: 4
6: 4
    """

    layers = Solution.process_input(input_raw)
    assert Solution.part1(layers) == 24


def test_day13_part2():
    input_raw = """
0: 3
1: 2
4: 4
6: 4
    """

    layers = Solution.process_input(input_raw)
    assert Solution.part2(layers) == 10
