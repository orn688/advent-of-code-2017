from solutions import day3


def test_day3_part1():
    test_cases = {
        1: 0,
        12: 3,
        16: 3,
        18: 3,
        23: 2,
        24: 3,
        25: 4,
        1024: 31,
    }

    for address, expected in test_cases.items():
        assert day3.part1(address) == expected


def test_day3_part2():
    test_cases = {
        1: 2,
        2: 4,
        23: 25,
        59: 122,
        351: 362,
    }

    for address, expected in test_cases.items():
        assert day3.part2(address) == expected
