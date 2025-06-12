# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        meet_node = None
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                meet_node = fast
                break
        if not meet_node:
            return None
        # Find the entry point of the cycle
        start = head
        while start != meet_node:
            start = start.next
            meet_node = meet_node.next
        return start





if __name__ == "__main__":
    # Example usage:
    # Creating a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # Creates a cycle

    solution = Solution()
    cycle_node = solution.detectCycle(node1)
    if cycle_node:
        print(f"Cycle detected at node with value: {cycle_node.val}")
    else:
        print("No cycle detected")
