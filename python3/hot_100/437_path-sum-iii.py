from typing import Optional

from datastructure.tree import TreeNode


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        # prefix_count will store the number of times a prefix sum has occurred
        prefix_count = {0: 1}

        def dfs(node: Optional[TreeNode], currSum: int):
            if not node:
                return
            currSum += node.val
            self.count += prefix_count.get(currSum - targetSum, 0)

            prefix_count[currSum] = prefix_count.get(currSum, 0) + 1
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            prefix_count[currSum] -= 1

        dfs(root, 0)
        return self.count

    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        def dfs_from(node: Optional[TreeNode], currentSum: int) -> int:
            if not node:
                return 0

            currentSum += node.val
            if currentSum == targetSum:
                self.ans += 1
            dfs_from(node.left, currentSum)
            dfs_from(node.right, currentSum)
            return 0

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            dfs_from(node, 0)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.ans


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
    result = solution.pathSum(root, targetSum)
    print(result)  # Expected output: Number of paths that sum to targetSum
