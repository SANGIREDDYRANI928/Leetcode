class Solution(object):
    def combine(self, n, k):
        ans=[]
        def backtrack(curr,start,visited):
            if len(curr)==k:
                ans.append(curr[:])
                return
            for i in range(start,n+1):
                if visited[i]:
                    continue
                visited[i]=True
                curr.append(i)
                backtrack(curr,i+1,visited)
                curr.pop()
                visited[i]=False
        visited=[False]*(n+1)
        backtrack([],1,visited)
        return ans




        