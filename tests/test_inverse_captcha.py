from solutions import inverse_captcha


def test_inverse_captcha_part1():
    test_cases = {
        '': 0,
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9,
    }

    for sequence, expected in test_cases.items():
        assert inverse_captcha.part1(sequence) == expected


def test_inverse_captcha_part2():
    test_cases = {
        '': 0,
        '1212': 6,
        '1221': 0,
        '123425': 4,
        '123123': 12,
        '12131415': 4,
    }

    for sequence, expected in test_cases.items():
        assert inverse_captcha.part2(sequence) == expected
