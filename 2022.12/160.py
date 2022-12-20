from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummyA, dummyB = headA, headB
        while dummyA is not None or dummyB is not None:
            dummyA = dummyA.next
            dummyB = dummyB.next

        if dummyA is None:
            while dummyB is not None:
                dummyB = dummyB.next
                headB = headB.next
        if dummyB is None:
            while dummyA is not None:
                dummyA = dummyA.next
                headA = headA.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headB
