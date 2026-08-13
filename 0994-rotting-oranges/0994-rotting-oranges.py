from collections import deque
class Solution:
    def orangesRotting(self, grid):
        queue=deque()
        fresh=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        minutes=0
        directions=[
            (-1,0),(1,0),(0,-1),(0,1)
        ]
        while queue and fresh>0:
            size=len(queue)
            for _ in range(size):
                i,j=queue.popleft()
                for dr,dc in directions:
                    nr=dr+i
                    nc=dc+j
                    if(0<=nr<n and 0<=nc<m and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            minutes+=1
        if fresh==0:
            return minutes
        return -1

        