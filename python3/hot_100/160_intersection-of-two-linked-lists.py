# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pointer_a, pointer_b = headA, headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA
        return pointer_a


if __name__ == '__main__':
    # Example usage:
    # Creating two linked lists that intersect
    nodeA1 = ListNode(4)
    nodeA2 = ListNode(1)
    nodeB1 = ListNode(5)
    nodeB2 = ListNode(0)
    nodeB3 = ListNode(1)
    intersection = ListNode(8)
    nodeA1.next = nodeA2
    nodeA2.next = intersection
    nodeB1.next = nodeB2
    nodeB2.next = nodeB3
    nodeB3.next = intersection
    intersection.next = ListNode(4)

    solution = Solution()
    intersection_node = solution.getIntersectionNode(nodeA1, nodeB1)
    if intersection_node:
        print(f"Intersection at node with value: {intersection_node.val}")
    else:
        print("No intersection")
