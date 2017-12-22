from solutions.day11 import Solution


def test_day11_part1():
    test_cases = {
        'ne,ne,ne': 3,
        'ne,ne,sw,sw': 0,
        'ne,ne,s,s': 2,
        'se,sw,se,sw,sw': 3,
    }

    for path, expected_distance in test_cases.items():
        path_list = Solution.process_input(path)
        assert Solution.part1(path_list) == expected_distance


def test_day11_part2():
    test_cases = {
        'ne,ne,ne': 3,
        'ne,ne,sw,sw': 2,
        'ne,ne,s,s,nw,nw': 2,
        'se,sw,se,sw,sw': 3,
    }

    for path, expected_distance in test_cases.items():
        path_list = Solution.process_input(path)
        assert Solution.part2(path_list) == expected_distance
