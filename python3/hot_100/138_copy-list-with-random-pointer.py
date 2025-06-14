from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        cur =  head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = old_to_new[cur]
            new_node.next = old_to_new.get(cur.next)
            new_node.random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new.get(head)



if __name__ == '__main__':
    # Example usage:
    # Creating a linked list with random pointers
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.random = node3
    node2.random = node1
    node3.random = None
    node4.random = node2

    solution = Solution()
    copied_head = solution.copyRandomList(node1)

    # Print the copied linked list
    current = copied_head
    while current:
        print(f"Node value: {current.val}, Random value: {current.random.val if current.random else None}")
        current = current.next
