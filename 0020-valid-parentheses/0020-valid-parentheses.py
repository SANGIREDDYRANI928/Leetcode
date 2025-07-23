class Solution:
    def isValid(self, s):
        stack=[]
        dict1={'}':'{',')':'(',']':'['}
        for i in s:
            if i in dict1:
                if stack:
                 top=stack.pop()
                 if dict1[i]!=top:
                    return False
                else:
                    return False
            else:
                stack.append(i)
        return not stack

        