import heapq
class Solution(object):
    def minimumCost(self, nums):
        start=nums[0]
        n=len(nums)
        mini=[]
        for i in range(1,n):
            heapq.heappush(mini,nums[i])
        return start+heapq.heappop(mini)+heapq.heappop(mini)

        