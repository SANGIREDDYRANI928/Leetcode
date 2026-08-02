class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)

        dp = piles[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(
                    piles[i] - dp[j],
                    piles[j] - dp[j - 1]
                )

        return dp[n - 1] > 0