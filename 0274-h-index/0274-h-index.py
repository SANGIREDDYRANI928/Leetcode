class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()
        for i in range(n):
            papers=n-i
            if citations[i]>=papers:
                return papers
        return 0