class Solution:
    def canConstruct(self, ransomNote, magazine) :
        dictA={}
        dictB={}
        for i in ransomNote:
            if i in dictA:
                dictA[i]+=1
            else:
                dictA[i]=1
        for i in magazine:
            if i in dictB:
                dictB[i]+=1
            else:
                dictB[i]=1
        c=0
        for i in dictA:
            if i in dictB:
                if dictA[i]<=dictB[i]:
                    c+=(dictA[i])
        if(c==len(ransomNote)):
            return True
        else:
            return False

        