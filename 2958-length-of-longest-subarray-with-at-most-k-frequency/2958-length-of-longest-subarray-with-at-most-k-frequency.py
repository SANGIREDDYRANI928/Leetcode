from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums,k):
        dict1={}
        n=len(nums)
        left=0
        ans=0
        for i in range(n):
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
            while dict1[nums[i]]>k:
                dict1[nums[left]]-=1
                left+=1
            ans=max(ans,i-left+1)
        return ans

        