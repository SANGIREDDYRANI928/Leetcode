class Solution:
    def summaryRanges(self, nums):
        if len(nums)==0:
            return []
        start=nums[0]
        n=len(nums)
        ans=[]
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                continue
            else:
                end=nums[i-1]
                if start==end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start=nums[i]
        end=nums[-1]
        if start==end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans

        