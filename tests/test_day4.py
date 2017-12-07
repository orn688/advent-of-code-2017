from solutions import day4


def test_day4_part1():
    test_cases = {
        ('aa bb cc dd ee',): 1,
        ('aa bb cc dd aa',): 0,
        ('aa bb cc dd aaa',): 1,
    }

    for passphrases, expected in test_cases.items():
        assert day4.part1(passphrases) == expected



def test_day4_part2():
    test_cases = {
        ('abcde fghij',): 1,
        ('abcde xyz ecdab',): 0,
        ('a ab abc abd abf abj',): 1,
        ('iiii oiii ooii oooi oooo',): 1,
        ('oiii ioii iioi iiio',): 0,
    }

    for passphrases, expected in test_cases.items():
        assert day4.part2(passphrases) == expected
