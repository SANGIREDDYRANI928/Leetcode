class Solution(object):
    def permute(self, nums):
        n=len(nums)
        used=[False]*n
        ans=[]
        def backtrack(current):
            if len(current)==len(nums):
                ans.append(current[::])
                return
            for i in range(n):
                if used[i]:
                    continue
                current.append(nums[i])
                used[i]=True
                backtrack(current)
                current.pop()
                used[i]=False
        backtrack([])
        return ans
        