import heapq
class Solution(object):
    def networkDelayTime(self,times,n,k):
        graph=[[] for _ in range(n+1)]
        dist=[float('inf')]*(n+1)
        for src,dst,wei in times:
            graph[src].append((dst,wei))
        heap=[(0,k)]
        dist[k]=0
        while heap:
            curr_dist,node=heapq.heappop(heap)
            if curr_dist>dist[node]:
                continue
            for nei,wt in graph[node]:
                new_dist=curr_dist+wt
                if new_dist<dist[nei]:
                    dist[nei]=new_dist
                    heapq.heappush(heap,(new_dist,nei))
        for i in range(1,n+1):
            if dist[i]==float('inf'):
                return -1
        return max(dist[1:])
        