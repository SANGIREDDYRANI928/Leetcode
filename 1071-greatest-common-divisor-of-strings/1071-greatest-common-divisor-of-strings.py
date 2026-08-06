from math import gcd
class Solution:
    def gcdOfStrings(self,str1,str2):
        if(str1+str2!=str2+str1):
            return ""
        n1=len(str1)
        n2=len(str2)
        x=gcd(n1,n2)
        return str1[0:x]
        

        