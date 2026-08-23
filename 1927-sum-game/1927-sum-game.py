class Solution:
    def sumGame(self, num):
        left_sum=0
        right_sum=0
        left_q=0
        right_q=0
        n=len(num)
        for i in range(n):
            if i<n//2:
                if num[i]=='?':
                    left_q+=1
                else:
                    left_sum+=int(num[i])
            else:
                if num[i]=='?':
                    right_q+=1
                else:
                    right_sum+=int(num[i])
        if (left_q+right_q)%2==1:
            return True
        return left_sum - right_sum != (right_q - left_q) * 9 // 2