class Solution:
    def searchRange(self, nums, target):
        output=[]
        l=0
        h=len(nums)-1
        ans=-1
        while(l<=h):
            mid=(l+h)//2
            if nums[mid]>=target:
                h=mid-1
                ans=mid
            else:
                l=mid+1
        if ans != -1 and nums[ans] == target:
            output.append(ans)
        else:
            output.append(-1)
        l=0
        h=len(nums)-1
        ans=-1
        while(l<=h):
            mid=(l+h)//2
            if nums[mid]<=target:
                l=mid+1
                ans=mid
            else:
                h=mid-1
        if ans != -1 and nums[ans] == target:
            output.append(ans)
        else:
            output.append(-1)
        return output
        