import java.util.*;
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n=nums1.length;
        int[] ans=new int[n];
        Stack<Integer> s=new Stack<>();
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int num:nums2)
        {
            while(!s.isEmpty()&&num>s.peek())
            {
                int pre=s.pop();
                h.put(pre,num);
            }
            s.push(num);
        }
        while(!s.isEmpty())
        {
            int pre=s.pop();
            h.put(pre,-1);
        }
        for(int i=0;i<nums1.length;i++)
        {
            ans[i]=h.get(nums1[i]);
        }
        return ans;

        
    }
}