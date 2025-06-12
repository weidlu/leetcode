# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next



        #
        # h1 = list1
        # h2 = list2
        # dummy = ListNode()
        # while h1 and h2:
        #     if h1.val < h2.val:
        #         dummy.next = h1
        #         h1 = h1.next
        #     else:
        #         dummy.next = h2
        #         next_node = h2.next
        #         h2.next = None
        #         h2 = next_node
        # if h1 is not None:
        #     dummy.next = h1
        # elif h2 is not None:
        #     dummy.next = h2
        # return dummy.next



if __name__ == '__main__':
    # Example usage:
    # Creating two linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print the merged linked list
    current = merged_list
    while current:
        print(current.val, end=' ')
        current = current.next