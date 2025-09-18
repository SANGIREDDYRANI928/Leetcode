class Solution:
    def firstBadVersion(self, n) :
        l=1
        h=n
        ans=float('inf')
        while(l<=h):
            mid=(l+h)//2
            if(isBadVersion(mid)):
                ans=min(ans,mid)
                h=mid-1
            else:
                l=mid+1
        return ans

        