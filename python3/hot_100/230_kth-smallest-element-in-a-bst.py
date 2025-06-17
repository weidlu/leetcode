from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_list = []

        def in_order(node: Optional[TreeNode]):
            if node:
                in_order(node.left)
                in_order_list.append(node.val)
                in_order(node.right)

        in_order(root)

        return in_order_list[k - 1]

if __name__ == "__main__":
    # Example usage:
    # Creating a binary search tree:
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root = TreeNode(3)
    root.left = TreeNode(1, None, TreeNode(2))
    root.right = TreeNode(4)

    solution = Solution()
    result = solution.kthSmallest(root, 1)
    print(result)  # Expected output: 1
