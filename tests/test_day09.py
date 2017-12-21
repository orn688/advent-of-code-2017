from solutions.day09 import Solution


def test_day09_part1():
    test_cases = {
        '{}': 1,
        '{{{}}}': 6,
        '{{},{}}': 5,
        '{{{},{},{{}}}}': 16,
        '{<{},{},{{}}>}': 1,
        '{<a>,<a>,<a>,<a>}': 1,
        '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
        '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
        '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
    }

    for stream, expected_score in test_cases.items():
        assert Solution.part1(stream) == expected_score


def test_day09_part2():
    test_cases = {
        '<>': 0,
        '<random characters>': 17,
        '<<<<>': 3,
        '<{!>}>': 2,
        '<!!>': 0,
        '<!!!>>': 0,
        '<{o"i!a,<{i<a>': 10,
    }

    for stream, expected_garbage_count in test_cases.items():
        assert Solution.part2(stream) == expected_garbage_count
