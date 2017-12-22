"""
Day 11: Hex Ed
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 11

    @staticmethod
    def process_input(input_raw):
        return input_raw.split(',')

    @staticmethod
    def part1(steps):
        return Solution._travel_path(steps, part=1)

    @staticmethod
    def part2(steps):
        return Solution._travel_path(steps, part=2)

    @staticmethod
    def _travel_path(steps, part):
        north = 0
        east = 0
        max_distance = 0
        for step in steps:
            # Since a diagonal step involves traveling half the vertical
            # distance of an actual vertical step, considering diagonal steps
            # to change the vertical displacement by one unit and vertical
            # steps by 2 to avoid dealing with floats.
            if step == 'n':
                north += 2
            elif step == 's':
                north -= 2
            else:
                if step.startswith('n'):
                    north += 1
                else:
                    north -= 1

                if step.endswith('e'):
                    east += 1
                else:
                    east -= 1

            max_distance = max(max_distance,
                               Solution._distance_away(north, east))

        if part == 1:
            return Solution._distance_away(north, east)
        elif part == 2:
            return max_distance
        else:
            return None


    @staticmethod
    def _distance_away(north, east):
        """Determine minimum number of steps necessary to get to a hexagon
        `north` units north and `east` units east of the start point.

        We can only have gotten `east` units horizontally via exactly
        `abs(east)` diagonal moves, which also would have caused `abs(east)`
        units of vertical change, so we must travel the rest of the distance
        to the eventual location via vertical steps, each of which moves us
        up or down by 2 units. But all the vertical movement could also have
        happened as part of diagonal steps, so don't let this go below 0.
        """
        return abs(east) + max(0, abs(north) - abs(east)) // 2


if __name__ == '__main__':
    Solution.main()
