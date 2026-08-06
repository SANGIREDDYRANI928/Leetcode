import heapq
class Solution:
    def maximumProduct(self,nums,k):
        MOD=10**9+7
        heapify(nums)
        for i in range(k):
            x=heappop(nums)
            heappush(nums,x+1)
        ans=1
        for i in nums:
            ans=(ans*i)%MOD
        return ans
        

        