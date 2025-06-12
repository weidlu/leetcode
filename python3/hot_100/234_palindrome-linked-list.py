# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def find_middle_method_1(head):
    """常规法：while fast and fast.next"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def find_middle_method_2(head):
    """保守法：while fast.next and fast.next.next"""
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def test_case(values):
    head = create_list(values)
    m1 = find_middle_method_1(head)
    m2 = find_middle_method_2(head)
    print(f"链表：{values}")
    print(f"方法1（fast and fast.next）找中点：{m1}")
    print(f"方法2（fast.next and fast.next.next）找中点：{m2}")
    print('-' * 40)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # Compare the first half and the reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    # Example usage:
    # 测试用例
    test_case([1])
    test_case([1, 2])
    test_case([1, 2, 3])
    test_case([1, 2, 3, 4])
    test_case([1, 2, 3, 4, 5])
    test_case([1, 2, 3, 4, 5, 6])

    # Creating a linked list: 1 -> 2 -> 3 -> 2 -> 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next= ListNode(2)
    head.next.next.next = ListNode(1)
    # head.next.next.next.next = ListNode(1)

    solution = Solution()
    print(solution.isPalindrome(head))  # Expected output: True
