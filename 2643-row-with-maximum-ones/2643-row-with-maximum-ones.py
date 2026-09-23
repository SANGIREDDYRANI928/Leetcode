class Solution(object):
    def rowAndMaximumOnes(self, mat):
        count_index=0
        n=len(mat)
        m=len(mat[0])
        max_count=0
        for i in range(n):
            count_1=0
            for j in range(m):
                if mat[i][j]==1:
                    count_1+=1
            if count_1>max_count:
                count_index=i
                max_count=count_1
        l=[]
        l.append(count_index)
        l.append(max_count)
        return l

        