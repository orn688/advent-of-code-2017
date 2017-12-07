from solutions import day2


def test_day2_part1():
    test_cases = {
        '5 1 9 5\n7 5 3\n2 4 6 8': 18,
    }

    for spreadsheet, expected in test_cases.items():
        assert day2.part1(spreadsheet) == expected


def test_day2_part2():
    test_cases = {
        '5 9 2 8\n9 4 7 3\n3 8 6 5': 9,
    }

    for spreadsheet, expected in test_cases.items():
        assert day2.part2(spreadsheet) == expected
