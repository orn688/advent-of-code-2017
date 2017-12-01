import os
import requests


def main():
    session_id = os.environ['SESSION_ID']
    cookies = dict(session=session_id)

    input_url = 'http://adventofcode.com/2017/day/1/input'

    response = requests.get(input_url, cookies=cookies)
    sequence = response.text.strip()

    print(inverse_captcha(sequence))


def inverse_captcha(sequence):
    """
    Determine the sum of all the digits d in the sequence such that the digit
    immediately following d is equal to d. Note that the sequence is
    circular; i.e., the first digit is considered to follow the last digit.
    """
    total = 0

    for i, num in enumerate(sequence):
        next_num = sequence[(i + 1) % len(sequence)]
        if num == next_num:
            total += int(num)

    return total


if __name__ == '__main__':
    main()
