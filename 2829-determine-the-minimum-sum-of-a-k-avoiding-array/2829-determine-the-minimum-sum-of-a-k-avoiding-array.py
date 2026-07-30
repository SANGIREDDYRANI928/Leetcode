class Solution:
    def minimumSum(self, n,k):
        l=set()
        i=1
        while True:
            if n==len(l):
                break
            if k-i not in l:
                l.add(i)
                i+=1
            if k-i in l:
                i+=1
        return sum(l)

                  