"""
Day 4: High-Entropy Passphrases
"""
from collections import Counter


DAY = 4


def main():
    from utils import get_input_for_day

    passphrases = get_input_for_day(DAY).split('\n')

    print(f'Part 1: {part1(passphrases)}')
    print(f'Part 2: {part2(passphrases)}')


def part1(passphrases):
    """
    Determine how many of the passphrases are valid; i.e., contain no
    duplicate words.
    """
    valid_count = 0

    for passphrase in passphrases:
        words = passphrase.split()
        if len(words) == len(set(words)):
            valid_count += 1

    return valid_count


def part2(passphrases):
    """
    Determine how many of the passphrases contain no two words that are
    anagrams of each other.
    """
    valid_count = 0

    for passphrase in passphrases:
        words = passphrase.split()
        seen = set()

        for word in words:
            sorted_letters = ''.join(sorted(word))
            if sorted_letters not in seen:
                seen.add(sorted_letters)

        if len(seen) == len(words):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    main()
