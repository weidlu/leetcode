# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            result.next = ListNode(total % 10)
            result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


if __name__ == "__main__":
    # Example usage:
    # Creating two linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the resulting linked list
    current = result
    while current:
        print(current.val, end=' ')
        current = current.next
