# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    """
    This is exactly the same solution that I used for 236. Lowest Common Ancestor of a Binary Tree
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

    This solution will handle the case where p or q not in the tree
    """
    def __init__(self):
        self.lowest = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest = None
        self.search(root, p, q)

        return self.lowest

    def search(self, node: TreeNode, p: TreeNode, q: TreeNode) -> int:
        """
        Return the number of nodes out of p and q found in the current subtree rooted in node

        :param node: root of the current subtree
        :param p: first of the tree node to find
        :param q: second of the tree node to find
        :return: number of nodes found in the current subtree
        """
        if not node:
            return 0

        l, r = self.search(node.left, p, q), self.search(node.right, p, q)
        if node == p or node == q:
            if l + r + 1 == 2:
                self.lowest = node

            return l + r + 1
        else:
            if l > 0 and r > 0:
                self.lowest = node

            return l + r


def main():
    root = TreeNode(3)
    root.left, root.right = TreeNode(5), TreeNode(1)
    root.left.left, root.left.right, root.right.left, root.right.right = TreeNode(6), TreeNode(2), TreeNode(
        0), TreeNode(8)
    root.left.right.left, root.left.right.right = TreeNode(7), TreeNode(4)

    s = Solution()
    print(s.lowestCommonAncestor(root, root.left, root.left.right))
    print(s.lowestCommonAncestor(root, root.left, TreeNode(4)))


if __name__ == "__main__":
    main()
