class Solution(object):
    def subsets(self, nums):
        ans=[]
        def backtrack(start,current):
            ans.append(current[:])
            for i in range(start,len(nums)):
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        current=[]
        backtrack(0,current)
        return ans
        