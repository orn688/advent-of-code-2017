from solutions import high_entropy_passphrases


def test_high_entropy_passphrases_part1():
    test_cases = {
        ('aa bb cc dd ee',): 1,
        ('aa bb cc dd aa',): 0,
        ('aa bb cc dd aaa',): 1,
    }

    for passphrases, expected in test_cases.items():
        assert high_entropy_passphrases.part1(passphrases) == expected



def test_high_entropy_passphrases_part2():
    test_cases = {
        ('abcde fghij',): 1,
        ('abcde xyz ecdab',): 0,
        ('a ab abc abd abf abj',): 1,
        ('iiii oiii ooii oooi oooo',): 1,
        ('oiii ioii iioi iiio',): 0,
    }

    for passphrases, expected in test_cases.items():
        assert high_entropy_passphrases.part2(passphrases) == expected
