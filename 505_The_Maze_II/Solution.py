from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        start, destination = tuple(start), tuple(destination)
        row, col = len(maze), len(maze[0])

        def neighbors(maze, node):
            temp = []
            used = set()
            used.add(node)
            for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                (x, y), dist = node, 0
                while 0 <= x + dx < row and 0 <= y + dy < col and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                if (x, y) not in used:
                    temp.append((dist, (x, y)))
            return temp

        heap = [(0, start)]
        visited = set()
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited: continue
            if node == destination:
                return dist
            visited.add(node)
            for neighbor_dist, neighbor in neighbors(maze, node):
                heapq.heappush(heap, (dist + neighbor_dist, neighbor))

        return -1