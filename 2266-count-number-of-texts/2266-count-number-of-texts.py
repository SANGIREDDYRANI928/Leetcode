class Solution:
    def countTexts(self, pressedKeys):
        MOD = 10**9 + 7
        n = len(pressedKeys)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):

            # Press current key once
            dp[i] = dp[i - 1]

            # Press it twice
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] += dp[i - 2]

            # Press it three times
            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
                dp[i] += dp[i - 3]

            # Keys 7 and 9 have 4 letters
            if i >= 4 and pressedKeys[i - 1] in "79":
                if (pressedKeys[i - 1] == pressedKeys[i - 2] ==
                    pressedKeys[i - 3] == pressedKeys[i - 4]):
                    dp[i] += dp[i - 4]

            dp[i] %= MOD

        return dp[n]