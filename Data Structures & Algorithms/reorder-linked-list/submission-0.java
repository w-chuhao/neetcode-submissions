/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {

        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next;
            fast = fast.next;
        }

        ListNode mid = slow.next;
        slow.next = null;

        ListNode prev = null;

        while(mid!=null){
            ListNode nextNode = mid.next;
            mid.next = prev;
            prev = mid;
            mid = nextNode;
        }

        ListNode curr = head;
        ListNode curr1 = prev;

        while(curr1!=null){
            ListNode nxtNode = curr.next;
            ListNode nxtNode1 = curr1.next;
            curr.next = curr1;
            curr1.next = nxtNode;
            curr = nxtNode;
            curr1 = nxtNode1;
        } 
    }
}
