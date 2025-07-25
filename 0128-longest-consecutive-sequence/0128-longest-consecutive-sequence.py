class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        c=list(set(nums))
        c.sort()
        c1=1
        ans=0
        if not nums:
            return 0
        for i in range(1,len(c)):
            if c[i]==c[i-1]+1:
                c1+=1
            else:
                ans=max(ans,c1)
                c1=1
        ans=max(ans,c1)
        return ans




        