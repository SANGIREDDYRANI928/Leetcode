import java.util.*;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> h=new HashSet<>();
        while(headB!=null)
        {
            h.add(headB);
            headB=headB.next;
        }
        while(headA!=null)
        {
            if (h.contains(headA))
            {
                return headA;
            }
            headA=headA.next;
        }
        return null;

        
    }
}