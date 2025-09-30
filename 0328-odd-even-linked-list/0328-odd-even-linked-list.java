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
    public ListNode oddEvenList(ListNode head) {
        ListNode dummy=new ListNode(-1,null);
        ListNode dummy1=new ListNode(-1,null);
        ListNode e=dummy;
        ListNode o=dummy1;
        ListNode h=head;
        int index=1;
        while(h!=null)
        {
            if (index%2==0)
            {
                e.next=h;
                e=e.next;
            }
            else{
                o.next=h;
                o=o.next;
            }
            h=h.next;
            index+=1;
        }
        e.next=null;
        o.next=dummy.next;
        return dummy1.next;
        
    }
}