"""
Day 14: Disk Defragmentation
"""
from solution_base import SolutionBase
import day10


knot_hash = day10.Solution.part2
GRID_SIZE = 128


class Solution(SolutionBase):
    day = 14

    @staticmethod
    def process_input(input_raw):
        key = input_raw
        grid = []

        for row in range(GRID_SIZE):
            hash_input = f'{key}-{row}'
            row_hash = knot_hash(hash_input)
            bits = bin(int(row_hash, 16))[2:].zfill(GRID_SIZE)
            grid.append([int(bit) for bit in bits])

        return grid

    @staticmethod
    def part1(grid):
        return sum(row.count(1) for row in grid)

    @staticmethod
    def part2(grid):
        visited = set()
        group_count = 0

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == 1 and (row, col) not in visited:
                    Solution._traverse_group(grid, visited, (row, col))
                    group_count += 1

        return group_count

    @staticmethod
    def _traverse_group(grid, visited, start_coords):
        stack = [start_coords]
        visited.add(start_coords)

        while stack:
            coords = stack.pop()
            for row, col in Solution._neighbors(coords):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    stack.append((row, col))

    @staticmethod
    def _neighbors(coords):
        row, col = coords
        if row > 0:
            yield (row - 1, col)
        if row < GRID_SIZE - 1:
            yield (row + 1, col)
        if col > 0:
            yield (row, col - 1)
        if col < GRID_SIZE - 1:
            yield (row, col + 1)


if __name__ == '__main__':
    Solution.main()
