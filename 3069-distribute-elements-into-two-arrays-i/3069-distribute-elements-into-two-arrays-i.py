class Solution:
    def resultArray(self,nums):
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        n=len(nums)
        j=2
        while j<n:
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[j])
            else:
                arr2.append(nums[j])
            j+=1
        res=[]
        m1=len(arr1)
        m2=len(arr2)
        for i in range(m1):
            res.append(arr1[i])
        for i in range(m2):
            res.append(arr2[i])
        return res

        