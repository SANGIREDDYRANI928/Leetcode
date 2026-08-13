class Solution:
    def mergeAlternately(self, word1,word2):
        s1=""
        n=len(word1)
        m=len(word2)
        p1=0
        p2=0
        while(p1<n and p2<m):
            if p1==p2:
                s1+=word1[p1]
                p1+=1
            elif p1<p2:
                s1+=word1[p1]
                p1+=1
            elif p2<p1:
                s1+=word2[p2]
                p2+=1
        if p1<n:
            while p1<n:
                s1+=word1[p1]
                p1+=1
        if p2<m:
            while p2<m:
                s1+=word2[p2]
                p2+=1
        return s1
        