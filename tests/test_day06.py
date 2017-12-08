from solutions import day06


def test_day06_part1():
    test_cases = {
        (0, 2, 7, 0): 5,
    }

    for banks, expected in test_cases.items():
        assert day06.part1(list(banks)) == expected


def test_day06_part2():
    test_cases = {
        (0, 2, 7, 0): 4,
    }

    for banks, expected in test_cases.items():
        assert day06.part2(list(banks)) == expected
