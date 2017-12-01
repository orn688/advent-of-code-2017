from inverse_captcha import inverse_captcha


def test_inverse_captcha():
    test_cases = {
        '': 0,
        '1122': 3,
        '1111': 4,
        '1234': 0,
        '91212129': 9,
    }

    for sequence, expected in test_cases.items():
        assert inverse_captcha(sequence) == expected
