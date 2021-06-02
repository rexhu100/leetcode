"""
Author: Huahua
Running time: 207 ms
"""

class Solution:
    def pourWater(self, heights, V, K):
        def drop(h, K):
            best = K
            for d in (-1, 1):
                i = K + d
                while i >= 0 and i < len(h) and h[i] <= h[i - d]:
                    if h[i] < h[best]:
                        best = i
                    i += d
                if best != K:
                    break
            heights[best] += 1

        for _ in range(V):
            drop(heights, K)
        return heights