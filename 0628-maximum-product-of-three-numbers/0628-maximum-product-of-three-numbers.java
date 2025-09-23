import java.util.Arrays;

class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        
        // Option 1: product of three largest numbers
        int prod1 = nums[n-1] * nums[n-2] * nums[n-3];
        
        // Option 2: product of two smallest and the largest
        int prod2 = nums[0] * nums[1] * nums[n-1];
        
        return Math.max(prod1, prod2);
    }
}
