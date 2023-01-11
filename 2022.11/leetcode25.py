# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode(object):
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class Solution(object):
    def reverseK(self, headA, headB):
        pre, cur, nxt = None, headA, headA
        while cur != headB:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        a, b = head, head
        for i in range(k):
            if b is None:
                return head
            else:
                b = b.next
        new_head = self.reverseK(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head


if __name__ == "__main__":
    n1 = ListNode(1, None)
    n2 = ListNode(2, None)
    n3 = ListNode(3, None)
    n4 = ListNode(4, None)
    n5 = ListNode(5, None)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    # r = s.reverseKGroup(n1, 2)

    r1 = s.reverseK(n1, n3)
    print(r1)
