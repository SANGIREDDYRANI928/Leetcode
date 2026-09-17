import heapq
class Solution(object):
    def kClosest(self,points,k):
        h=[]
        ans=[]
        for point in points:
            x=point[0]
            y=point[1]
            dist=sqrt((0-x)**2+(0-y)**2)
            heapq.heappush(h,(dist,x,y))
        for i in range(k):
            _,x,y=heapq.heappop(h)
            ans.append([x,y])
        return ans
