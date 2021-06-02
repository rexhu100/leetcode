"""
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each
index is 1. After V units of water fall at index K, how much water is at each index? Water first drops at index K and
rests on top of the highest terrain or water at that index. Then, it flows according to the following rules: If the
droplet would eventually fall by moving left, then move left. Otherwise, if the droplet would eventually fall by
moving right, then move right. Otherwise, rise at it's current position. Here, "eventually fall" means that the
droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the
terrain plus any water in that column. We can assume there's infinitely high terrain on the two sides out of bounds
of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of
water has to be in exactly one block.

link
https://leetcode.jp/problemdetail.php?id=755
"""
from typing import List
from Solution import Solution


def pour_water(heights: List[int], V, K) -> List[int]:
    water_levels = heights.copy()
    for _ in range(V):
        filled_left = False
        filled_right = False
        i = K
        while i > 0:
            if water_levels[i-1] < water_levels[i]:
                filled_left = True
                water_levels[i - 1] += 1
                break
            elif water_levels[i-1] > water_levels[i]:
                break

            i -= 1

        if not filled_left:
            while i < len(water_levels)-1:
                if water_levels[i + 1] < water_levels[i]:
                    filled_right = True
                    water_levels[i + 1] += 1
                    break
                elif water_levels[i + 1] > water_levels[i]:
                    break

                i += 1

        if not filled_left and not filled_right:
            water_levels[K] += 1

    return water_levels


def main():
    heights = [2, 1, 1, 2, 1, 2, 2]
    V = 4
    K = 3
    sol = Solution()
    print(sol.pourWater(heights.copy(), V, K))
    print(pour_water(heights.copy(), V, K))

    heights = [1, 2, 3, 4]
    V = 2
    K = 2
    print(sol.pourWater(heights.copy(), V, K))
    print(pour_water(heights.copy(), V, K))

    heights = [3, 1, 3]
    V = 5
    K = 1
    print(sol.pourWater(heights.copy(), V, K))
    print(pour_water(heights.copy(), V, K))

    heights = [0, 1, 2, 0, 0, 2]
    V = 4
    K = 4
    print(sol.pourWater(heights.copy(), V, K))
    print(pour_water(heights.copy(), V, K))


if __name__ == "__main__":
    main()