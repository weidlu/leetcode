from datastructure.tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        return left if left else right  # If one side is None, return the other side (which could be None or the LCA)


if __name__ == "__main__":
    # Example usage:
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with value 5
    q = root.right  # Node with value 1

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)  # Expected output: 3 (the LCA of nodes 5 and 1 is 3)
