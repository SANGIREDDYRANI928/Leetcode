class Solution:
    def findMaxConsecutiveOnes(self, nums) :
        c=0
        ans=-math.inf
        for i in nums:
            if i==1:
                c+=1
                ans=max(ans,c)
            else:
                c=0
        if c>ans:
            return c
        else:
            return ans
        