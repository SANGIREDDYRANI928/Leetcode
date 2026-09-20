class Solution(object):
    def jump(self, nums):
        jumps=0
        end=0
        farthest=0
        n=len(nums)
        for i in range(n-1):
            farthest=max(farthest,nums[i]+i)
            if end==i:
                jumps+=1
                end=farthest
        return jumps

        