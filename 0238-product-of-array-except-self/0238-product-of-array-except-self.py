class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        pp=[]
        sp=[0]*n
        b=[0]*n
        pp.append(nums[0])
        for i in range(1,n):
            pp.append(pp[i-1]*nums[i])
        sp[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            sp[i]=sp[i+1]*nums[i]
        b[0]=sp[1]  
        b[n-1]=pp[n-2]
        for i in range(1,n-1):
            b[i]=pp[i-1]*sp[i+1]
        return b