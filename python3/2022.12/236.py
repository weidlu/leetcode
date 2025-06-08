class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.find(root, p.val, q.val)

    def find(self, root: TreeNode, val1: int, val2: int) -> TreeNode:
        if not root:
            return root
        if root.val == val1 or root.val == val2:
            return root
        l_node: TreeNode
        r_node: TreeNode
        l_node = self.find(root.left, val1, val2)
        r_node = self.find(root.right, val1, val2)
        if not l_node and not r_node:
            return None
        if not l_node and r_node:
            return r_node
        if not r_node and l_node:
            return l_node
        return root  # if l_node and r_node
