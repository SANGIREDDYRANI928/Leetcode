class Solution:
    def addBinary(self, a, b):
        A=len(a)-1
        B=len(b)-1
        carry=0
        result=[]
        while(A>=0 or B>=0):
            sum1=carry
            if A>=0:
                sum1+=int(a[A])
                A+=-1
            if B>=0:
                sum1+=int(b[B])
                B+=-1
            result.append(str(sum1%2))
            carry=sum1//2
        if (carry==1):
            result.append(str(1))
        return ''.join(reversed(result))
            
        