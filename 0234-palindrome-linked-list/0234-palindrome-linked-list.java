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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode nextNode = curr.next; 
            curr.next = prev;             
            prev = curr;                   
            curr = nextNode;               
        }

        return prev;
    }
    public boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null)
        {
            return true;
        }
        ListNode mid=FindMid(head);
        ListNode h2=reverseList(mid.next);
        mid.next=null;
        ListNode p1 = head;
        ListNode p2 = h2;
        boolean palindrome = true;

        while (p2 != null) {
            if (p1.val != p2.val) {
                palindrome = false;
                break;
            }
            p1 = p1.next;
            p2 = p2.next;
    
        
        }
        return palindrome;
    }
     public ListNode FindMid(ListNode head)
    {
        if (head==null)
        {
            return head;
        }
        ListNode slow=head;
        ListNode fast=head;
        while(fast.next!=null && fast.next.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;

        }
        return slow;

    }
}