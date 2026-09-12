class Solution(object):
    def minimumOperations(self, nums):
        set1=set()
        for i in nums:
            if i!=0:
                set1.add(i)
        return len(set1)
        