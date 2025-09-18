class Solution:
    def findTheDifference(self, s, t) :
        dictA={}
        dictB={}
        for i in s:
            if i in dictA:
                dictA[i]+=1
            else:
                dictA[i]=1
        for i in t:
            if i in dictB:
                dictB[i]+=1
            else:
                dictB[i]=1
        for i in dictB:
            if i in dictA:
                if dictA[i]==dictB[i]:
                    continue
                else:
                    return i
            else:
                return i

        