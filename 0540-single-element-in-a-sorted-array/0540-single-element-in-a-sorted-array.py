class Solution:
    def singleNonDuplicate(self, nums):
        xor=0
        for i in nums:
            xor=xor^i
        return xor
        