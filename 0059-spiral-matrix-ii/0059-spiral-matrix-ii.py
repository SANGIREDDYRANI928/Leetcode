class Solution(object):
    def generateMatrix(self, n):
        matrix=[[0]*n for _ in range(n)]
        top=0
        left=0
        bottom=n-1
        right=n-1
        value=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                matrix[top][i]=value
                value+=1
            top+=1
            for j in range(top,bottom+1):
                matrix[j][right]=value
                value+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=value
                    value+=1
                bottom-=1
            if left<=right:
                for j in range(bottom,top-1,-1):
                    matrix[j][left]=value
                    value+=1
                left+=1
        return matrix
        