"""There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next
direction. Given the ball's start position, the destination and the maze, find the shortest distance for the ball to
stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start
position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1. The maze is
represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of
the maze are all walls. The start and destination coordinates are represented by row and column indexes. """
from typing import List
from Solution import Solution
import heapq


def shortest_dist(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    destination = tuple(destination)
    start = tuple(start)
    m, n = len(maze), len(maze[0])
    directions = [0, 1, 0, -1, 0]
    dist = [[float("inf")] * n for _ in range(m)]
    dist[start[0]][start[1]] = 0
    pq = [(0, start)]

    while pq:
        d, (r, c) = heapq.heappop(pq)
        if (r, c) == destination:
            return d

        if d > dist[r][c]:
            continue

        for i in range(4):
            nextr, nextc = r, c
            nextd = -1
            while 0 <= nextr < m and 0 <= nextc < n and maze[nextr][nextc] != 1:
                nextr, nextc = nextr + directions[i], nextc + directions[i + 1]
                nextd += 1

            if nextd > 0:
                nextr, nextc = nextr - directions[i], nextc - directions[i + 1]
                if dist[r][c] + nextd < dist[nextr][nextc]:
                    dist[nextr][nextc] = dist[r][c] + nextd
                    heapq.heappush(pq, (dist[r][c] + nextd, (nextr, nextc)))

    return -1


def main():
    test_maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    sol = Solution()

    print(sol.shortestDistance(test_maze, start, destination))
    print(shortest_dist(test_maze, start, destination))

    # start = [0, 4]
    # destination = [3, 2]
    #
    # print(sol.shortestDistance(test_maze, start, destination))
    # print(shortest_dist(test_maze, start, destination))
    #
    # test_maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    # start = [4, 3]
    # destination = [0, 1]
    #
    # print(sol.shortestDistance(test_maze, start, destination))
    # print(shortest_dist(test_maze, start, destination))


if __name__ == "__main__":
    main()
