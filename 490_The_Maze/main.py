"""There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go
through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the
ball stops, it could choose the next direction. Given the maze, the ball's start position and the destination,
where start = [start_row, start_col] and destination = [destination_row, destination_col], return true if the ball can
stop at the destination, otherwise return false. You may assume that the borders of the maze are all walls (see
examples). """
from typing import List
from collections import deque
from Solution import Solution


def has_path(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    destination = tuple(destination)
    start = tuple(start)
    m, n = len(maze), len(maze[0])
    directions = (0, 1, 0, -1, 0)
    frontier = deque([start])

    def get_next(r, c):
        ret = {(r, c)}
        for i in range(4):
            nextr, nextc = r, c
            while 0 <= nextr < m and 0 <= nextc < n and maze[nextr][nextc] != 1:
                nextr += directions[i]
                nextc += directions[i + 1]

            nextr -= directions[i]
            nextc -= directions[i + 1]

            ret.add((nextr, nextc))

        ret.remove((r, c))

        return ret

    seen = [[False] * n for _ in range(m)]
    while frontier:
        r, c = frontier.popleft()
        if (r, c) == destination:
            return True

        seen[r][c] = True
        for nextr, nextc in get_next(r, c):
            if not seen[nextr][nextc]:
                frontier.append((nextr, nextc))

    return False


def main():
    test_maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    sol = Solution()

    print(sol.hasPath(test_maze, start, destination))
    print(has_path(test_maze, start, destination))

    start = [0, 4]
    destination = [3, 2]

    print(sol.hasPath(test_maze, start, destination))
    print(has_path(test_maze, start, destination))

    test_maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    start = [4, 3]
    destination = [0, 1]

    print(sol.hasPath(test_maze, start, destination))
    print(has_path(test_maze, start, destination))


if __name__ == "__main__":
    main()
