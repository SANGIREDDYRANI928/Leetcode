class Solution:
    def findWords(self, words) :
        row1=['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']

        row2=['A','S','D','F','G','H','J','K','L','a','s','d','f','g','h','j','k','l']

        row3=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        output=[]
        
        for s in words:
            c1=0
            c2=0
            c3=0
            for j in range(len(s)):
                if s[j] in row1:
                    c1+=1
                elif s[j] in row2:
                    c2+=1
                else:
                    c3+=1
            if c1==len(s) or c2==len(s) or c3==len(s):
                output.append(s)
        return output

        