from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        dict1=Counter(tasks)
        maxi=max(dict1.values())
        c=0
        for i in dict1.values():
            if i==maxi:
                c+=1
        part=(maxi-1)*(n+1)+c
        return max(len(tasks),part)

        