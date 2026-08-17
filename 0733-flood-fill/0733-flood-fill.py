class Solution:
    def floodFill(self,image,sr,sc,color):
        n=len(image)
        m=len(image[0])
        original=image[sr][sc]
        if original==color:
            return image
        def dfs(i,j,color,image):
            if i<0 or i>=n or j<0 or j>=m:
                return 
            if image[i][j]!=original:
                return
            image[i][j]=color
            dfs(i-1,j,color,image)
            dfs(i+1,j,color,image)
            dfs(i,j-1,color,image)
            dfs(i,j+1,color,image)

        
        dfs(sr,sc,color,image)
        return image
        