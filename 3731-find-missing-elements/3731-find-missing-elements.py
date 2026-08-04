class Solution:
    def findMissingElements(self, nums):
        maxi=max(nums)
        mini=min(nums)
        n=len(nums)
        set1=set(nums)
        l=[]
        while(mini<=maxi):
            if mini not in set1:
                l.append(mini)
            mini+=1
        return l
        