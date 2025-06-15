# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node: Optional[TreeNode]):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter


if __name__ == "__main__":
    # Example usage:
    # Creating a binary tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)

    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    print(diameter)  # Expected output: 3 (the path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
