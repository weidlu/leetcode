from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = l_move = ListNode(-1)
        great = g_move = ListNode(-1)

        while head is not None:
            tmp = head
            head = head.next
            tmp.next = None
            if tmp.val < x:
                l_move.next = tmp
                l_move = l_move.next
            else:
                g_move.next = tmp
                g_move = g_move.next

        l_move.next = great.next
        return less.next


if __name__ == "__main__":
    input = [1, 4, 3, 2, 5, 2]
    # input = []
    dummy = h = ListNode(-1)
    for i in input:
        h.next = ListNode(i)
        h = h.next
    s = Solution()
    new_head = s.partition(dummy.next, 3)
    print(new_head)
