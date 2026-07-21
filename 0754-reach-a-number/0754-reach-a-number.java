class Solution {
   
    public int reachNumber(int target) {
        target=Math.abs(target);
        int sum1=0;
        int steps=0;
        while(sum1<target || (sum1-target)%2!=0)
        {
            steps+=1;
            sum1+=steps;
        }
        return steps;
   
}}