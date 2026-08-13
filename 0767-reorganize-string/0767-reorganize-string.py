import heapq
from collections import Counter
class Solution:
    def reorganizeString(self,s):
        n=len(s)
        max_heap=[]
        dict1=Counter(s)
        for key,value in dict1.items():
            heapq.heappush(max_heap,(-value,key))
        if -max_heap[0][0]>(n+1)//2:
            return ""
        ans=[]
        prev_count=0
        prev_char=""
        while max_heap:
            count,char=heapq.heappop(max_heap)
            count+=1
            ans.append(char)

            if prev_count<0:
                heapq.heappush(max_heap,(prev_count,prev_char))
            prev_count=count
            prev_char=char
        return "".join(ans)