class Solution:
    def smallestNumber(self, n,t):
        def product(n):
            prod=1
            s=str(n)
            leng=len(s)
            for i in range(leng):
                prod=(prod*int(s[i]))
            return prod
        while(True):
            x=product(n)
            print(x)
            if x%t==0:
                return n
            n=n+1


        