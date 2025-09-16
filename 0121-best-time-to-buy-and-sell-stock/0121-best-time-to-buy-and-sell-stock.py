import math
class Solution:
    def maxProfit(self, prices):
        mini=float('inf')
        maxi=0
        for i in prices:
            mini=min(mini,i)
            maxi=max(maxi,i-(mini))
        return maxi
        