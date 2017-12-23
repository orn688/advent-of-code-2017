from solutions.day12 import Solution


def test_day12_part1():
    input_raw = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

    graph = Solution.process_input(input_raw)
    assert Solution.part1(graph) == 6


def test_day12_part2():
    input_raw = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

    graph = Solution.process_input(input_raw)
    assert Solution.part2(graph) == 2
