class Solution:
    def isPalindrome(self, x):
        y=x
        rev=0
        while(x>0):
            rev=rev*10+(x%10)
            x=x//10
        if(rev==abs(y)):
            return True
        else:
            return False
obj=Solution()
print(obj.isPalindrome(121))


        