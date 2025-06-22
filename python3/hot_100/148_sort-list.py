# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        q = head
        while q:
            val.append(q.val)
            q = q.next
        val.sort()

        dummy = ListNode()
        p = dummy
        for i in range(len(val)):
            p.next = ListNode(val[i])
            p = p.next
        p.next = None
        return dummy.next


if __name__ == '__main__':
    # Example usage:
    # Creating a linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    solution = Solution()
    sorted_head = solution.sortList(head)

    # Print the sorted linked list
    current = sorted_head
    while current:
        print(current.val, end=' ')
        current = current.next
