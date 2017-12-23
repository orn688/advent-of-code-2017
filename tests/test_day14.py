from solutions.day14 import Solution


def test_day14_part1():
    grid = Solution.process_input('flqrgnkx')
    assert Solution.part1(grid) == 8108


def test_day14_part2():
    grid = Solution.process_input('flqrgnkx')
    assert Solution.part2(grid) == 1242
