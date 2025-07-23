class Solution:
    def trap(self, height):
        pm=[]
        sm=[0]*(len(height))
        pm.append(height[0])
        for i in range(1,len(height)):
            pm.append(max(pm[i-1],height[i]))
        sm[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            sm[i]=max(height[i],sm[i+1])
        sum1=0
        for i in range(len(height)):
            sum1=sum1+min(pm[i],sm[i])-height[i]
        return sum1
        