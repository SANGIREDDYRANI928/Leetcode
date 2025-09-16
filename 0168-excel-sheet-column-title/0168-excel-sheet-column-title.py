class Solution:
    def convertToTitle(self, columnNumber) :

        res=[]
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            ans=res.append(chr(ord('A')+rem))
            columnNumber=columnNumber//26
        return ''.join(reversed(res))

        