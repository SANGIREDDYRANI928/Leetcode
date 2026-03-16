class Solution:
    def shuffle(self, nums, n):
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[n+i])
        return l