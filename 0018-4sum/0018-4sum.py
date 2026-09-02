class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=n-1
                while(left<right):
                    sum1=nums[left]+nums[right]+nums[i]+nums[j]
                    if(sum1==target):
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif sum1<target:
                        left+=1
                    else:
                        right-=1
        return ans

        