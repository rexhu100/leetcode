# Definition for a binary tree node.
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    @staticmethod
    def serialize(root: TreeNode) -> List:
        """
        Encodes a tree to a single string.

        :param root:
        :return:
        """
        if not root:
            return []

        coded = []
        frontier = [root]
        while frontier:
            next_frontier = []
            for node in frontier:
                if node:
                    next_frontier.extend([node.left, node.right])
                    coded.append(node.val)
                else:
                    coded.append(None)

            frontier = next_frontier

        while coded[-1] is None:
            coded.pop()

        return coded

    @staticmethod
    def deserialize(data: List) -> TreeNode:
        """
        Decodes your encoded data to tree.

        :param data:
        :return:
        """
        if not data:
            return None

        # print(data)
        root = TreeNode(data[0])
        frontier = [root]
        offset = 0
        data_index = 0

        ctr = 2
        while frontier:
            next_frontier = []
            for node in frontier:

                if not node:
                    data_index += 1
                    offset += 1
                    continue

                l, r = (data_index - offset) * 2 + 1, (data_index - offset) * 2 + 2
                if l < len(data):
                    node.left = TreeNode(data[l]) if data[l] is not None else None
                else:
                    node.left = None

                if r < len(data):
                    node.right = TreeNode(data[r]) if data[r] is not None else None
                else:
                    node.right = None

                data_index += 1
                next_frontier.extend([node.left, node.right])

            frontier = next_frontier

            # if ctr == 0:
            #     break
            # ctr -= 1

        return root