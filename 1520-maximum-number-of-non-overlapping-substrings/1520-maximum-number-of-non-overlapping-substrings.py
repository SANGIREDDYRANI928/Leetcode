class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # first and last occurrence
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Find smallest valid interval for each character
        for c in range(26):

            if first[c] == n:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character appeared before left,
                # so this interval cannot be valid.
                if first[x] < left:
                    valid = False
                    break

                # Need to include all occurrences of this character
                right = max(right, last[x])

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans