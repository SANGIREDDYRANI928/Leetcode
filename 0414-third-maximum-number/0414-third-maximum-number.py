import heapq

class Solution:
    def thirdMax(self, nums):

        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        nums = [-x for x in nums]

        heapq.heapify(nums)

        heapq.heappop(nums)   # largest
        heapq.heappop(nums)   # second largest

        return -heapq.heappop(nums)   # third largest