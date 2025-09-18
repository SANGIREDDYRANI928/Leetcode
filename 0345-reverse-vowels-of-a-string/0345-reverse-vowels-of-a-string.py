class Solution:
    def reverseVowels(self, s) :
        v=['a','e','i','o','u','A','E','I','O','U']
        l,h=0,len(s)-1
        li=list(s)
        while(l<h):
            while l<h and li[l] not in v:
                l+=1 
            while l<h and li[h] not in v:
                h-=1
            li[l],li[h]=li[h],li[l]
            l+=1
            h-=1
        return ''.join(li)        