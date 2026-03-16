class Solution:
    def longestOnes(self, nums, k):
        zero_count=0
        max_count=-float('inf')
        c=0
        left=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
                if zero_count<=k:
                    c+=1
            if nums[i]==1:
                c+=1
            while zero_count>k:
                if nums[left]==1:
                    c-=1
                if nums[left]==0:
                    zero_count-=1
                left+=1 
            max_count=max(max_count,c)
        return max_count
                

        