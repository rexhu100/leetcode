class Solution(object):
    def numIslands2(self, n, m, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        def find(res, p):
            while p != res[p]:
                p = res[p]
                res[p] = res[res[p]]
            return p

        def connected(res, p, q):
            return find(res, p) == find(res, q)

        def union(res, p, q):
            pid = find(res, p)
            qid = find(res, q)
            res[pid] = qid

        res = [i for i in range(m * n)]
        visited = [0 for i in range(m * n)]
        out = []
        grid = [[0] * m for i in range(n)]

        count = 0
        counter = 0
        for i, j in positions:
            counter += 1
            index = i * m + j
            if visited[index] == 1:
                count -= 1
            grid[i][j] = 1
            queue = [index]
            while queue:
                temp = queue.pop(0)
                visited[temp] = 1
                r = temp // m
                c = temp % m
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    if not connected(res, temp, ((r - 1) * m + c)):
                        union(res, temp, ((r - 1) * m + c))
                        queue.append((r - 1) * m + c)
                        count -= 1
                if r + 1 < n and grid[r + 1][c] == 1:
                    if not connected(res, temp, ((r + 1) * m + c)):
                        union(res, temp, ((r + 1) * m + c))
                        queue.append((r + 1) * m + c)
                        count -= 1
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    if not connected(res, temp, (r * m + c - 1)):
                        union(res, temp, (r * m + c - 1))
                        queue.append(r * m + c - 1)
                        count -= 1
                if c + 1 < m and grid[r][c + 1] == 1:
                    if not connected(res, temp, (r * m + c + 1)):
                        union(res, temp, (r * m + c + 1))
                        queue.append(r * m + c + 1)
                        count -= 1
            out.append(counter + count)

        return out