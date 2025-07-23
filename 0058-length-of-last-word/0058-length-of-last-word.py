class Solution:
    def lengthOfLastWord(self, s):
        string=s.split()
        return(len(string[-1]))
        