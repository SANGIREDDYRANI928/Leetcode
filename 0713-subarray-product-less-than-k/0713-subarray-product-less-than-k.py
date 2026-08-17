class Solution:
    def numSubarrayProductLessThanK(self,nums,k):
        if k<=1:
            return 0
        n=len(nums)
        left=0
        prod=1
        ans=0
        for right in range(n):
            prod*=nums[right]
            while prod>=k:
                prod//=nums[left]
                left+=1
            ans+=right-left+1
        return ans


        