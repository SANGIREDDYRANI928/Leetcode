import heapq
class Solution(object):
    def lastStoneWeight(self,stones):
        s=[-x for x in stones]
        heapq.heapify(s)
        while len(s)>1:
            top1=heapq.heappop(s)
            top2=heapq.heappop(s)
            if top1==top2:
                continue
            else:
                heapq.heappush(s,-abs((-top1)-(-top2)))
        if s:
            return -s[0]
        else:
            return 0
        