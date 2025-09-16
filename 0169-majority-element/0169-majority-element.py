class Solution:
    def majorityElement(self, nums) :
        dictA=dict()
        for i in nums:
            if i in dictA:
                dictA[i]+=1
            else:
                dictA[i]=1
        limit=len(nums)//2
        for i in dictA:
            if dictA[i]>limit:
                return i
        