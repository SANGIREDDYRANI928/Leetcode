class Solution:
    def sequentialDigits(self, low, high):
        ans = []
        s = "123456789"

        for length in range(2, 10):
            for i in range(len(s)-length+1):
                num = int(s[i:i+length])

                if low <= num <= high:
                    ans.append(num)

        return sorted(ans)