class Solution(object):
    def findErrorNums(self, nums):
        h={}
        for i in range(1,len(nums)+1):
            h[i]=0
            
        h1=set()
        l=[]
        for i in range(0,len(nums)):
            h[nums[i]]+=1
            if nums[i] not in h1:
                h1.add(nums[i])
            else:
                l.append(nums[i])
        for i in h:
            if h[i]==0:
                l.append(i)
        return l

        