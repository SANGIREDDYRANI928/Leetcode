from collections import Counter
class Solution:
    def arrayRankTransform(self,arr):
        n=len(arr)
        rank=[0]*n
        dict1=dict()
        arr1=arr[:]
        arr1.sort()
        c=1
        print(arr1)
        print(arr)
        for i in arr1:
            if i in dict1:
                continue
            else:
                dict1[i]=c
                c+=1
        for i in range(n):
            rank[i]=dict1[arr[i]]
        return rank

        


        
        