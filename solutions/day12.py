"""
Day 12: Digital Plumber
"""
from collections import deque
from solution_base import SolutionBase


class Solution(SolutionBase):
    day = 12

    @staticmethod
    def process_input(input_raw):
        graph = dict()

        for line in input_raw.strip().split('\n'):
            node, neighbors = line.split(' <-> ')
            graph[int(node)] = [int(n) for n in neighbors.split(', ')]

        return graph

    @staticmethod
    def part1(graph):
        seen = set([0])
        queue = deque([0])

        while queue:
            curr = queue.popleft()

            for neighbor in graph[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return len(seen)

    @staticmethod
    def part2(graph):
        not_seen = set(graph)
        group_count = 0

        while not_seen:
            group_count += 1

            root = not_seen.pop()
            queue = deque([root])

            while queue:
                curr = queue.popleft()

                for neighbor in graph[curr]:
                    if neighbor in not_seen:
                        not_seen.remove(neighbor)
                        queue.append(neighbor)

        return group_count


if __name__ == '__main__':
    Solution.main()
