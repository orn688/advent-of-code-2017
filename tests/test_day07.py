from solutions.day07 import Solution


def test_day06_part1():
    test_input = (
        'pbga (66)\n'
        'xhth (57)\n'
        'ebii (61)\n'
        'havc (66)\n'
        'ktlj (57)\n'
        'fwft (72) -> ktlj, cntj, xhth\n'
        'qoyq (66)\n'
        'padx (45) -> pbga, havc, qoyq\n'
        'tknk (41) -> ugml, padx, fwft\n'
        'jptl (61)\n'
        'ugml (68) -> gyxo, ebii, jptl\n'
        'gyxo (61)\n'
        'cntj (57)'
    )

    programs = Solution.process_input(test_input)
    assert Solution.part1(programs) == 'tknk'


def test_day06_part2():
    test_input = (
        'pbga (66)\n'
        'xhth (57)\n'
        'ebii (61)\n'
        'havc (66)\n'
        'ktlj (57)\n'
        'fwft (72) -> ktlj, cntj, xhth\n'
        'qoyq (66)\n'
        'padx (45) -> pbga, havc, qoyq\n'
        'tknk (41) -> ugml, padx, fwft\n'
        'jptl (61)\n'
        'ugml (68) -> gyxo, ebii, jptl\n'
        'gyxo (61)\n'
        'cntj (57)'
    )

    programs = Solution.process_input(test_input)
    assert Solution.part2(programs) == 60
