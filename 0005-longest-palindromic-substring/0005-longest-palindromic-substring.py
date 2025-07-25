import math
class Solution:
    def generate(self,s,n,x,y):
        p1=x
        p2=y
        while(p1>=0 and p2<n):
            if s[p1]==s[p2]:
                p1-=1
                p2+=1
            else:
                break
        return p2-p1-1
    def longestPalindrome(self, s):
        n=len(s)
        leng=-math.inf
        for i in range(n):
            oddlen=self.generate(s,n,i,i)
            evenlen=self.generate(s,n,i-1,i)
            current_length=max(oddlen,evenlen)
            if current_length>leng:
                leng=current_length
                start=(i-(int(current_length)//2))
        
            
        return s[start:start+leng]    