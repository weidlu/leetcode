from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        res = []
        _reversed = False
        while len(q) > 0:
            _size = len(q)
            level = []
            for _ in range(_size):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if _reversed:
                level.reverse()
                res.append(level)
            else:
                res.append(level)
            _reversed = not _reversed
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root9 = TreeNode(9)
    root20 = TreeNode(20)
    root15 = TreeNode(15)
    root7 = TreeNode(7)

    root.left = root9
    root.right = root20
    root20.left = root15
    root20.right = root7

    s = Solution()
    r = s.zigzagLevelOrder(root)
    print(r)
