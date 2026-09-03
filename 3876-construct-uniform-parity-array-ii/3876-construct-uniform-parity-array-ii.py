class Solution:
    def uniformArray(self, nums1):
        nums1.sort()

        target = nums1[0] % 2
        seen = [False, False]
        seen[target] = True

        for i in range(1, len(nums1)):
            x = nums1[i]

            if x % 2 != target:
                required = (x % 2) ^ target

                if not seen[required]:
                    return False

            seen[x % 2] = True

        return True