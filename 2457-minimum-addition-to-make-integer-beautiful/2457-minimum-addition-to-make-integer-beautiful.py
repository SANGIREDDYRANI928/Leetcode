class Solution:
    def makeIntegerBeautiful(self,n,target):
        def sumnum(n):
            sum1=0
            s=str(n)
            n=len(s)
            for i in range(n):
                sum1+=int(s[i])
            return sum1
        ans=0
        base=1
        while(sumnum(n)>target):
            base*=10
            rounded=(n//base+1)*base
            ans+=rounded-n
            n=rounded
        return ans




        