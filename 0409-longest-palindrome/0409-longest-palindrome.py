class Solution:
    def longestPalindrome(self, s):
        dictA={}
        for i in s:
            if i in dictA:
                dictA[i]+=1
            else:
                dictA[i]=1
        c=0
        c_1=0
        for i in dictA:
            if dictA[i]%2==0:
                c+=dictA[i]
            elif dictA[i]>2:
                c+=((dictA[i]//2)*2)
                c_1+=1
            else:
                c_1+=1
        if c_1>0:
            return c+1
        if c>0:
            return c
        else:
            return c_1

        