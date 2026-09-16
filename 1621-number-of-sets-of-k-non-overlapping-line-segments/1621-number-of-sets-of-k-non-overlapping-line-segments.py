class Solution:
    def numberOfSets(self, n,k):
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        # 0 segments -> 1 way
        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n):
                # dp[0][j-1] + ... + dp[i-1][j-1]
                prefix = (prefix + dp[i - 1][j - 1]) % MOD

                # Don't use point i
                dp[i][j] = dp[i - 1][j]

                # Use i as right endpoint
                dp[i][j] = (dp[i][j] + prefix) % MOD

        return dp[n - 1][k]