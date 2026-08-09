class Solution:
    def balancedStringSplit(self,s):
        prefix=[]
        l=[]
        n=len(s)
        for i in range(n):
            if s[i]=='L':
                l.append(1)
            else:
                l.append(-1)
        prefix.append(l[0])
        print(l)
        for i in range(1,n):
            prefix.append(prefix[i-1]+l[i])
        c=0
        print(prefix)
        for i in prefix:
            if i==0:
                c+=1
        return c
        