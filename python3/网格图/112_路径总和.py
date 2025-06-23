from typing import Optional

from datastructure.tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if targetSum == root.val and not root.left and not root.right:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


if __name__ == "__main__":
    # Example usage:
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    targetSum = 22
    solution = Solution()
    result = solution.hasPathSum(root, targetSum)
    print(result)  # Expected output: True (5 -> 4 -> 11 -> 2) or (5 -> 8 -> 4 -> 1) path exists
