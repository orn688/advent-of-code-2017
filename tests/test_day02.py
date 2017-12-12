from solutions.day02 import Solution


def test_day02_part1():
    test_cases = {
        ((5, 1, 9, 5), (7, 5, 3), (2, 4, 6, 8)): 18,
    }

    for spreadsheet, expected in test_cases.items():
        assert Solution.part1(spreadsheet) == expected


def test_day02_part2():
    test_cases = {
        ((5, 9, 2, 8), (9, 4, 7, 3), (3, 8, 6, 5)): 9,
    }

    for spreadsheet, expected in test_cases.items():
        assert Solution.part2(spreadsheet) == expected
