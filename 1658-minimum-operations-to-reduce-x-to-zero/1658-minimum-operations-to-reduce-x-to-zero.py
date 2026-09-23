class Solution(object):
    def minOperations(self, nums, x):
        sum1=sum(nums)
        target=sum1-x
        left=0
        maxlen=-1
        n=len(nums)
        if sum1==target:
            return n
        if target<0:
            return -1
        curr=0
        for right in range(n):
            curr+=nums[right]
            while curr>target:
                curr-=nums[left]
                left+=1
            if curr==target:
                maxlen=max(maxlen,right-left+1)
        if maxlen==-1:
            return -1
        return n-maxlen

        