"""
Day 13: Packet Scanners
"""
from collections import OrderedDict
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 13

    @staticmethod
    def process_input(input_raw):
        layers = OrderedDict()

        for layer_info in input_raw.strip().split('\n'):
            depth, scan_range = layer_info.split(': ')
            layers[int(depth)] = int(scan_range)

        return layers

    @staticmethod
    def part1(layers):
        total_severity = 0
        for depth, scan_range in layers.items():
            # The time it takes for a scanner to go from the top of its range
            # to the bottom and back; it spends 2 picoseconds at every point
            # (one on the way up and one on the way down) except the top and
            # the bottom.
            period = scan_range * 2 - 2

            # The depth of this layer is equal to the time at which you reach
            # it, and if the time you reach it is a multiple of the period then
            # the scanner gets there at that time, so you are caught.
            if depth % period == 0:
                total_severity += depth * scan_range

        return total_severity

    @staticmethod
    def part2(layers):
        delay = 0

        while True:
            caught = False # We haven't yet gotten caught on this layer.

            for depth, scan_range in layers.items():
                period = scan_range * 2 - 2

                if (depth + delay) % period == 0:
                    caught = True
                    break

            if caught:
                delay += 1
            else:
                return delay


if __name__ == '__main__':
    Solution.main()
