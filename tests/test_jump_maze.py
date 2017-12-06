from solutions import jump_maze


def test_jump_maze_part1():
    test_cases = {
        (0, 3, 0, 1, -3): 5,
        (-1, 2): 1,
    }

    for jumps, expected in test_cases.items():
        assert jump_maze.part1(list(jumps)) == expected


def test_jump_maze_part2():
    test_cases = {
        (0, 3, 0, 1, -3): 10,
        (-1, 2): 1,
        (3, 0, -3, -3): 4,
    }

    for jumps, expected in test_cases.items():
        assert jump_maze.part2(list(jumps)) == expected
