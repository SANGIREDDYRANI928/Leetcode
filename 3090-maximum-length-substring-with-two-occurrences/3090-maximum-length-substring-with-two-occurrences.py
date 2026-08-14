class Solution:
    def maximumLengthSubstring(self, s):
        dict1={}
        left=0
        n=len(s)
        ans=0
        for right in range(n):
            if s[right] in dict1:
                dict1[s[right]]+=1
            else:
                dict1[s[right]]=1
            while dict1[s[right]]>2:
                dict1[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
            


        