class Solution:
    def minimumAbsDifference(self, arr):
        min_dist=float('inf')
        n=len(arr)
        arr.sort()
        for i in range(1,n):
            min_dist=min(min_dist,arr[i]-arr[i-1])
        l=[]
        for i in range(1,n):
            if arr[i]-arr[i-1]==min_dist:
                l.append([arr[i-1],arr[i]])
        return l

        