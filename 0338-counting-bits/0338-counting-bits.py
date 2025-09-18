class Solution:
    def countBits(self, n):
        l=[]
        for i in range(n+1):
            x=bin(i)
            count_1=x.count('1')
            l.append(count_1)
        return l
        