"""
Day 10: Stream Processing
"""
from functools import reduce
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 10

    @staticmethod
    def part1(lengths_string, nums=None):
        lengths = [int(length) for length in lengths_string.split(',')]

        if not nums:
            nums = list(range(256))

        pos = 0
        skip_size = 0

        for reverse_length in lengths:
            for i in range(reverse_length // 2):
                left = (pos + i) % len(nums)
                right = (pos + reverse_length - 1 - i) % len(nums)
                nums[left], nums[right] = nums[right], nums[left]

            pos = (pos + reverse_length + skip_size) % len(nums)
            skip_size += 1

        return nums[0] * nums[1]

    @staticmethod
    def part2(input_string, nums=None):
        lengths = [ord(c) for c in input_string]
        extra_lengths = [17, 31, 73, 47, 23]
        lengths += extra_lengths

        if not nums:
            nums = list(range(256))

        pos = 0
        skip_size = 0

        for _ in range(64):
            for reverse_length in lengths:
                for i in range(reverse_length // 2):
                    left = (pos + i) % len(nums)
                    right = (pos + reverse_length - 1 - i) % len(nums)
                    nums[left], nums[right] = nums[right], nums[left]

                pos = (pos + reverse_length + skip_size) % len(nums)
                skip_size += 1

        dense_hash = []
        for i in range(0, len(nums), 16):
            sub_list = nums[i:(i + 16)]
            hash_num = reduce(lambda x, y: x ^ y, sub_list)
            hash_hex = (hex(hash_num)[2:]).zfill(2)
            dense_hash.append(hash_hex)

        return ''.join(dense_hash)


if __name__ == '__main__':
    Solution.main()
