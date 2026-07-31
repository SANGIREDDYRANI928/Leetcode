from collections import Counter 
class Solution:
    def minimumPushes(self, word):

        dict1=Counter(word)
        sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))

        ans=0
        j=0
        for i in sorted_dict:
            ans+=(sorted_dict[i]*((j//8)+1))
            j+=1
        return ans
    

        