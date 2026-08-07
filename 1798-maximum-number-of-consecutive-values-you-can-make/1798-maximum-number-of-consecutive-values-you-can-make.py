class Solution:
    def getMaximumConsecutive(self, coins):
        coins.sort()
        x=1
        for i in coins:
            if i>x:
                break
            x+=i
        return x


        