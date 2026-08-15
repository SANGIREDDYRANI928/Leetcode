class Solution:
    def findMaxLength(self, nums):
        dict1={0:-1}
        ans=0
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if count in dict1:
                ans=max(ans,i-dict1[count])
            else:
                dict1[count]=i
        return ans

        