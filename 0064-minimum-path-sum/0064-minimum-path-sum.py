class Solution(object):
    def minPathSum(self, grid):
        n=len(grid)
        m=len(grid[0])
        dp=[[0]*m for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for j in range(1,n):
            dp[j][0]=dp[j-1][0]+grid[j][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[n-1][m-1]
        