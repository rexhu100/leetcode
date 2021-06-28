"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their
concatenation equals target. If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in
target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
"""
from Solution import Solution


# Naive solution O(m*n)
def shortest_way(source: str, target: str) -> int:
    res = 1
    i, j = 0, 0

    while j < len(target):
        # The biggest slowdown of this implementation is that find takes O(m) time. If we can bring this down to O(1),
        # then we will have the optimal solution.
        i_next = source.find(target[j], i)
        if i_next == -1:
            if i == 0:
                return -1

            res += 1
            i = 0
        else:
            i = i_next + 1
            j += 1

    return res


def shortest_way_optimal(source: str, target: str) -> int:
    # We preprocess the data in source and build a hashmap that maps each index i and a character of source to the
    # index of the nearest location of the character to the right of i (inclusive). This is exactly what .find() is
    # doing in the previous implementation, and replacing that with this hashmap reduces the cost of the operation to
    # O(1).
    m, n = len(source), len(target)
    index_next_char = [{} for _ in range(m)]
    for i in range(m-1, -1, -1):
        index_next_char[i] = index_next_char[i + 1].copy() if i + 1 < m else {}
        index_next_char[i][source[i]] = i

    res = 1
    i, j = 0, 0
    while j < len(target):
        # The logic of the loop is unchanged from the previous implementation. We only change the .find(...) portion
        # with the hashmap we built above.
        if i == m:
            res += 1
            i = 0
        i_next = index_next_char[i].get(target[j], -1)

        if i_next == -1:
            if i == 0:
                return -1
            res += 1
            i = 0
        else:
            i = i_next + 1
            j += 1

    return res


def main():
    source = "abc"
    target = "abcbc"
    sol = Solution()
    print(shortest_way(source, target))
    print(shortest_way_optimal(source, target))
    print(sol.shortestWay(source, target))

    source = "abc"
    target = "abcbdc"
    print(shortest_way(source, target))
    print(shortest_way_optimal(source, target))
    print(sol.shortestWay(source, target))

    source = "xyzhtjaxxwery"
    target = "zyxzxyyzxyzxyzxyzyxyzyzzxyzxyzyxyzyxzyxyzyzxyzxyyzyzyxyzzxyzyxyyzyxzyxyzyxyzyyxyyxyzyxyyzxyyzyxyzyyxzyxyz"
    print(shortest_way(source, target))
    print(shortest_way_optimal(source, target))
    print(sol.shortestWay(source, target))


if __name__ == "__main__":
    main()