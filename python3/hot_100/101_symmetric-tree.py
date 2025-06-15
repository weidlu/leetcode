# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        if not root:
            return True
        return is_mirror(root.left, root.right)


if __name__ == "__main__":
    # Example usage:
    # Creating a symmetric binary tree:
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    solution = Solution()
    result = solution.isSymmetric(root)
    print(result)  # Expected output: True
