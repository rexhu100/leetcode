"""A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which
turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands
after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. """
from typing import List
from UnionFind import UF
from Solution import Solution


def num_islands2(n, m, positions: List[List[int]]) -> List[int]:
    def coord2ind(r, c) -> int:
        return n * r + c

    connectivity = UF(n * m)

    rd, cd = (0, 1, 0, -1), (1, 0, -1, 0)
    land_set = set()
    res = []
    for (row, col) in positions:
        total = res[-1] + 1 if res else 1
        root_set = set()
        for i in range(4):
            next_row = row + rd[i]
            next_col = col + cd[i]
            if next_row < 0 or next_row == m or next_col < 0 or next_col == n or (next_row, next_col) not in land_set:
                continue

            root_set.add(connectivity.get_root(coord2ind(next_row, next_col)))

        total -= len(root_set)
        # print(land_set)

        for i in range(4):
            next_row = row + rd[i]
            next_col = col + cd[i]
            if next_row < 0 or next_row == m or next_col < 0 or next_col == n or (row, col) not in land_set:
                continue

            connectivity.union(coord2ind(row, col), coord2ind(next_row, next_col))

        land_set.add((row, col))
        res.append(total)

    return res


def main():
    sol = Solution()
    m, n = 4, 3
    pos = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1], [3, 0]]
    print(num_islands2(n, m, pos))
    # print(sol.numIslands2(n, m, pos))  # This 'solution' gets an IndexError in some test cases


if __name__ == "__main__":
    main()
