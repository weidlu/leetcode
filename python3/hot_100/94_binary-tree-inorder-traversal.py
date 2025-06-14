# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        # cur is used to traverse the tree, and stack is used to keep track of nodes
        while cur or stack:
            # 一直向左压栈，直到碰到最左叶子
            while cur:
                stack.append(cur)
                cur = cur.left

            # 出栈并访问
            cur = stack.pop()
            res.append(cur.val)

            # 转向右子树，下一轮开始处理右子树的最左路径
            cur = cur.right
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                res.append(cur.val)
        return res


if __name__ == "__main__":
    # Example usage:
    # Creating a binary tree:
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.preorderTraversal(root)
    print(result)  # Expected output: [1, 3, 2]
