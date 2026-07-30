import heapq
class Solution:
    def maxWeight(self, pizzas):
        n=len(pizzas)
        p1=0
        p2=n-1
        days=n//4
        ans=0
        pizzas.sort()
        oddays=(days+1)//2
        evendays=days//2
        for i in range(oddays):
            p1+=3
            ans+=pizzas[p2]
            p2-=1
        for i in range(evendays):
            p1+=2
            ans+=pizzas[p2-1]
            p2-=2
        return ans

        