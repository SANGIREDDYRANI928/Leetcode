class Solution:
    def kidsWithCandies(self, candies,extraCandies):
        l=[]
        maxi=max(candies)
        n=len(candies)
        for i in range(n):
            if candies[i]+extraCandies>=maxi:
                l.append(True)
            else:
                l.append(False)
        return l
        