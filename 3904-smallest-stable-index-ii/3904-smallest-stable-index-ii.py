class Solution:
    def firstStableIndex(self,nums,k):
        n=len(nums)
        maxi=[0]*n
        mini=[0]*n
        maxi[0]=nums[0]
        if n==1 and k==0:
            return 0
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])
        mini[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])
        for i in range(n):
            if maxi[i]-mini[i]<=k:
                return i
        return -1
        