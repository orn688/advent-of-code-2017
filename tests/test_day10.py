from solutions.day10 import Solution


def test_day10_part1():
    lengths = '3,4,1,5'

    nums = list(range(5))
    assert Solution.part1(lengths, nums) == 12


def test_day10_part2():
    test_cases = {
        '': 'a2582a3a0e66e6e86e3812dcb672a272',
        'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
        '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
        '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e',
    }

    for input_string, expected_hash in test_cases.items():
        assert Solution.part2(input_string) == expected_hash
