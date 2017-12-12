"""
Day 3: Spiral memory
"""
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 3

    @staticmethod
    def process_input(input_raw):
        return int(input_raw)

    @staticmethod
    def part1(address):
        """
        Determine the number of steps from the center to the given address in
        a spirally allocated 2D memory space.
        """
        if address == 1:
            return 0

        curr_address = 2
        layer_num = 1

        while True:
            addresses_per_side = 2 * layer_num
            addresses_in_layer = 4 * addresses_per_side
            if curr_address + addresses_in_layer > address:
                break
            layer_num += 1
            curr_address += addresses_in_layer

        layer_start_down = layer_num - 1
        layer_start_right = layer_num

        index_in_layer = address - curr_address
        index_on_side = index_in_layer % addresses_per_side

        if index_in_layer < addresses_per_side:
            steps_down = layer_start_down - index_on_side
            steps_right = layer_start_right
        elif index_in_layer < 2 * addresses_per_side:
            steps_down = layer_start_down + 1 - addresses_per_side
            steps_right = layer_start_right - 1 - index_on_side
        elif index_in_layer < 3 * addresses_per_side:
            steps_down = -layer_start_down + index_on_side
            steps_right = -layer_start_right
        else:
            steps_down = layer_start_down + 1
            steps_right = -layer_start_right + 1 + index_on_side

        return abs(steps_down) + abs(steps_right)

    @staticmethod
    def part2(goal_value):
        """
        Determine the first value greater than goal_value written to memory
        if values are written in spiral order starting with 1 at address 1,
        and each value is the sum of the neighboring (already-written)
        values.
        """
        values = dict()
        values[(0, 0)] = 1

        coords = (1, 0)
        layer_num = 1
        edge = 0

        while True:
            value = 0
            for neighbor_coords in Solution._neighbors(coords):
                value += values.get(neighbor_coords, 0)

            values[coords] = value

            if value > goal_value:
                break
            else:
                if edge == 0: # Right
                    coords = (coords[0], coords[1] + 1)
                    if coords[1] == layer_num:
                        edge = 1
                elif edge == 1: # Top
                    coords = (coords[0] - 1, coords[1])
                    if coords[0] == -layer_num:
                        edge = 2
                elif edge == 2: # Left
                    coords = (coords[0], coords[1] - 1)
                    if coords[1] == -layer_num:
                        edge = 3
                elif edge == 3: # Bottom
                    coords = (coords[0] + 1, coords[1])
                    if coords[0] == layer_num + 1:
                        edge = 0
                        layer_num += 1

        return value

    @staticmethod
    def _neighbors(coords):
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == y == 0:
                    continue
                yield (coords[0] + x, coords[1] + y)


if __name__ == '__main__':
    Solution.main()
