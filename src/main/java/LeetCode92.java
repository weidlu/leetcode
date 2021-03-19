/**
 *
 */
public class LeetCode92 {

    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dump = new ListNode(-1);
        dump.next = head;

        ListNode preHead = dump;
        for (int i = 0; i < left - 1; i++) {
            preHead = preHead.next;
        }
        ListNode leftNode = preHead.next;

        ListNode rightNode = preHead;
        for (int i = 0; i < right - left + 1; i++) {
            rightNode = rightNode.next;
        }
        ListNode rightHead = rightNode.next;

        // reverse list from leftNode to rightNode
        preHead.next = null;
        rightNode.next = null;

        ListNode pre = preHead;
        ListNode cur = leftNode;
        ListNode nxt;
        while (cur != null){
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }

        preHead.next = rightNode;
        leftNode.next = rightHead;
        return dump.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode head2 = new ListNode(2);
        ListNode head3 = new ListNode(3);
        ListNode head4 = new ListNode(4);
        ListNode head5 = new ListNode(5);

        head.next = head2;
        head2.next = head3;
        head3.next = head4;
        head4.next = head5;


        LeetCode92 leetCode92 = new LeetCode92();
        leetCode92.reverseBetween(head, 2, 4);

        while (head != null) {
            System.out.println(head.val);
            head = head.next;
        }
    }
}
