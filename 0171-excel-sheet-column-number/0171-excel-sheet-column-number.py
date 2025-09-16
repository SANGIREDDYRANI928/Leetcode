class Solution:
    def titleToNumber(self, columnTitle):
        ans=0
        for i in columnTitle:
            res=(ord(i)-ord('A')+1)
            ans=ans*26+res
        return ans
        

        