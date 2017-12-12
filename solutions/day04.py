"""
Day 4: High-Entropy Passphrases
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 4

    @staticmethod
    def process_input(input_raw):
        return input_raw.split('\n')

    @staticmethod
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

    @staticmethod
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
    Solution.main()
