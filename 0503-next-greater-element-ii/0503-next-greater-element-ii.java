import java.util.*;
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length;
        int[] ans=new int[n];
        Arrays.fill(ans,-1);
        Stack<Integer> s=new Stack<>();
        for(int i=0;i<2*n;i++)
        {
            int x=i%n;
            while(!s.isEmpty()&&nums[x]>nums[s.peek()])
            {
              int idx=s.pop();
              ans[idx]=nums[x];
            }
            s.push(x);


        }
        return ans;
        
    }
}