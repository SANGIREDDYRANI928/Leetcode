class Solution:
    def toLowerCase(self, s) :
        s1=""
        for ch in s:
            if 65<=ord(ch)<=90:
                s1+=chr((ord(ch)^32))
                
            else:
                s1+=ch
                
            
        return s1
        