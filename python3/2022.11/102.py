import queue
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        res = []
        while not q.empty():
            size = q.qsize()
            l = []
            for i in range(size):
                node_i = q.get()
                l.append(node_i.val)
                if node_i.left is not None:
                    q.put(node_i.left)
                if node_i.right is not None:
                    q.put(node_i.right)
            res.append(l)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    node_9 = TreeNode(9)
    node_20 = TreeNode(20)
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    root.left = node_9
    root.right = node_20
    node_20.left = node_15
    node_20.right = node_7

    s = Solution()
    r = s.levelOrder(root)
    print(r)
