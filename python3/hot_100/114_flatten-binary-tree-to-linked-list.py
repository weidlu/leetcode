from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if prev is not None:
                prev.right = node
                prev.left = None

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node


if __name__ == "__main__":
    # Example usage:
    # Creating a binary tree:
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(5, None, TreeNode(6))

    solution = Solution()
    solution.flatten(root)

    # The flattened tree should look like:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
