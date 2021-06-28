class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)

        lis = [[-1] * 26 for _ in range(len(source))]
        for i in range(len(lis) - 1, -1, -1):
            if i == len(lis) - 1:
                lis[i][ord(source[i]) - ord('a')] = i
            else:
                lis[i][:] = lis[i + 1]
                lis[i][ord(source[i]) - ord('a')] = i

        ans = 1
        ind = 0
        for char in target:
            if char not in source_set:
                return -1
            if ind >= len(lis):
                ind = 0
                ans += 1

            ind = lis[ind][ord(char) - ord('a')]
            if ind == -1:
                ans += 1
                ind = 0
                ind = lis[ind][ord(char) - ord('a')]

            ind += 1

        return ans