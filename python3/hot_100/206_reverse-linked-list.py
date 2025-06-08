# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        current = head.next
        prev.next = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


if __name__ == '__main__':
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Print the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=' ')
        current = current.next
