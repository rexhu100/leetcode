from codec import Codec


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.longestArm(root)

        return self.res - 1

    def longestArm(self, node):
        """
        This function returns the length of longest univariate path starting from the root. It also has an important
        side effect, which is updating the longest univariate path anywhere in the tree.
        :param node: current tree node
        :return: length of the longest univariate path starting from the node
        """
        if not node:
            return 0

        l, r = self.longestArm(node.left), self.longestArm(node.right)
        cur_longest = 1
        cur_res = 1
        if node.left and node.left.val == node.val:
            cur_longest = max(cur_longest, l + 1)
            cur_res += l

        if node.right and node.right.val == node.val:
            cur_longest = max(cur_longest, r + 1)
            cur_res += r

        self.res = max(self.res, cur_res)

        return cur_longest


def main():
    test_tree = [1, 4, 5, 4, 4, None, 5, 4, 4]
    root = Codec.deserialize(test_tree)
    sol = Solution()
    print(sol.longestUnivaluePath(root))


if __name__ == "__main__":
    main()

