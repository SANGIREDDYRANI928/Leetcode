class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with just nums[i]
            r = num % k
            new_dp[r] += 1

            # Extend all previous subarrays
            for rem in range(k):
                new_rem = (rem * r) % k
                new_dp[new_rem] += dp[rem]

            # All subarrays ending here contribute to answer
            for rem in range(k):
                ans[rem] += new_dp[rem]

            dp = new_dp

        return ans