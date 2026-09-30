class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if(len(s)==0):
            return 1
        left=0
        right=0
        res=0
        se=set()
        while(right<len(s)):
            while(s[right] in se):
                se.remove(s[left])
                left+=1
            se.add(s[right])
            res=max(res,(right-left+1))
            right+=1
        return res
obj=Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))

        