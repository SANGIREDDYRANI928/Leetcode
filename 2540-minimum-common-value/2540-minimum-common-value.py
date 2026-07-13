class Solution:
    def getCommon(self,nums1,nums2):
        p1=0
        p2=0
        n=len(nums1)
        n1=len(nums2)
        while p1<n and p2<n1:
            if nums1[p1]==nums2[p2]:
                return nums1[p1]
            if nums1[p1]>nums2[p2]:
                p2+=1
            else:
                p1+=1 
        return -1
        
        