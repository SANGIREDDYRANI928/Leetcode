class Solution:
    def gen(self,n,even_count,odd_count,s,res):
        if n==even_count and n==odd_count:
            res.append(s)
            return
        if(even_count<n):
            self.gen(n,even_count+1,odd_count,s+'(',res)
        if odd_count<even_count:
            self.gen(n,even_count,odd_count+1,s+')',res)
    def generateParenthesis(self, n):
        res=[]
        self.gen(n,0,0,'',res)
        return res
    

        