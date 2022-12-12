from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    环形链表三连问：
    1.链表是否有环
    2.环的入口
    3.环中节点数量  这是一道数学题，参照（用chrome打开） https://codeantenna.com/a/A3h6Tgz0Zy#:~:text=%E7%AE%80%E5%8D%95%EF%BC%8C%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%E3%80%82-,3.%E8%AF%81%E6%98%8E,-%E4%B8%8B%E9%9D%A2%E6%88%91%E4%BB%AC%E6%9D%A5
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        if head is None:
            return False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # 确认有环，返回环的入口
    def cycleStartNode(self, head: Optional[ListNode]) -> ListNode:
        _fast = head
        _slow = head
        while _fast is not None and _fast.next is not None:
            _slow = _slow.next
            _fast = _fast.next.next
            if _fast == _slow:
                # 快慢相遇
                break
        _slow = head
        while _slow != _fast:
            _slow = _slow.next
            _fast = _fast.next
        return _slow


if __name__ == "__main__":
    head = ListNode(3)
    head2 = ListNode(2)
    head0 = ListNode(0)
    head4 = ListNode(-4)
    head.next = head2
    head2.next = head0
    head0.next = head4
    head4.next = head2

    s = Solution()
    re = s.cycleStartNode(head)
    print(re)
