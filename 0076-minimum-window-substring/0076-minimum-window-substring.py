from collections import Counter
class Solution:
    def minWindow(self,s,t):
        n=len(s)
        w={}
        t1=Counter(t)
        c=0
        ans=float('inf')
        left=0
        res=[-1,-1]
        for right in range(n):
            ch=s[right]
            w[ch]=w.get(ch,0)+1
            if ch in t1 and w[ch]==t1[ch]:
                c+=1 
            while c==len(t1) :
                if right-left+1<ans:
                    res=[left,right]
                    ans=right-left+1
                w[s[left]]-=1
                if s[left] in t1 and w[s[left]]<t1[s[left]]:
                    c-=1 
                left+=1
            l,r=res
        return s[l:r+1] if ans!=float('inf') else ""

            
            
        