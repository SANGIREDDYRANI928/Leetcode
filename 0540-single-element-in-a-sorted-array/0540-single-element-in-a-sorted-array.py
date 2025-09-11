class Solution:
    def singleNonDuplicate(self, nums):
        l, h = 0, len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if mid % 2 == 1:  # force mid to be even
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                h = mid
        return nums[l]
