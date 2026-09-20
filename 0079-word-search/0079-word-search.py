class Solution(object):
    def exist(self, board, word):
        startindex=0
        n=len(board)
        m=len(board[0])
        visited=[[False]*m for _ in range(n)]
        def backtrack(i,j,startindex):
            if i>=n or i<0 or j>=m or j<0:
                return False
            if visited[i][j] or word[startindex]!=board[i][j]:
                return False
            if startindex==len(word)-1:
                return True
            visited[i][j]=True
            if  backtrack(i-1,j,startindex+1) or backtrack(i+1,j,startindex+1) or backtrack(i,j-1,startindex+1) or backtrack(i,j+1,startindex+1):
                return True
            visited[i][j]=False
            return False
            
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[startindex]:
                    if backtrack(i,j,0):
                        return True
        return False
        