class Solution(object):
    def simplifyPath(self, path):
        p=path.split("/")
        stack=[]
        for i in p:
            if i=="" or i==".":
                continue
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+"/".join(stack)