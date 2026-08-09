class Solution:
    def countSubarrays(self, nums,minK,maxK):
        lastmin=-1
        lastmax=-1
        lastbad=-1
        n=len(nums)
        ans=0
        for i in range(n):
            if nums[i]<minK or nums[i]>maxK:
                lastbad=i
            if nums[i]==minK:
                lastmin=i
            if nums[i]==maxK:
                lastmax=i
            ans+=max(0,min(lastmin,lastmax)-lastbad)
        return ans
        
        