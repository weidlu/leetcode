# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        return head.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n11 = ListNode(1)
    n23 = ListNode(3)
    n34 = ListNode(4)
    n11.next = n23
    n23.next = n34

    s = Solution()
    h = s.mergeTwoLists(n1, n11)
    while h.next:
        print(h.val)
        h = h.next

