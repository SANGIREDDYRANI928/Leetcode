class Solution:
    def firstUniqChar(self, s):
        l={}
        for i in s:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i in range(len(s)):
            if l[s[i]]==1:
                return i
        return -1

        