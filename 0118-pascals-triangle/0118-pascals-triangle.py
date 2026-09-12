class Solution(object):
    def generate(self, numRows):
        ans=[]
        n=numRows
        for i in range(1,n+1):
            l=[1]*i
            for j in range(1,i-1):
                l[j]=ans[-1][j-1]+ans[-1][j]
            ans.append(l)
        return ans
        