class Solution:
    def transformArray(self, nums):
        count_even=0
        count_odd=0
        for i in nums:
            if i%2==0:
                count_even+=1
            else:
                count_odd+=1
        l=[]
        for i in range(count_even):
            l.append(0)
        for i in range(count_odd):
            l.append(1)
        return l
        