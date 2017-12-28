from solutions.day18 import Solution


def test_day18_part1():
    instructions = [
        ["set", "a", "1"],
        ["add", "a", "2"],
        ["mul", "a", "a"],
        ["mod", "a", "5"],
        ["snd", "a"],
        ["set", "a", "0"],
        ["rcv", "a"],
        ["jgz", "a", "-1"],
        ["set", "a", "1"],
        ["jgz", "a", "-2"],
    ]
    assert Solution.part1(instructions) == 4


def test_day18_part2():
    assert False
