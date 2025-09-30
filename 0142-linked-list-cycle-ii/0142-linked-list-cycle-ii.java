/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
            HashSet<ListNode> h=new HashSet<>();
            ListNode h1=head;
            while(h1!=null)
            {
                if (h.contains(h1)){
                    return h1;

                }
                h.add(h1);
                h1=h1.next;
            }
            return null;
        
    }
}