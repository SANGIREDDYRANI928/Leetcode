class Solution:
    def isSubsequence(self, s, t):
        p1=0
        p2=0
        c=0
        while(p1<len(s) and p2<len(t)):
            if s[p1]==t[p2]:
                c+=1
                p1+=1
                p2+=1
            elif s[p1]!=t[p2]:
                p2+=1
        if(c==len(s)):
            return True
        else:
            return False

            


        