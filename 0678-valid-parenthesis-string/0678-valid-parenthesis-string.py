class Solution(object):
    def checkValidString(self, s):

        low = 0
        high = 0

        for ch in s:

            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # We cannot have negative minimum
            if low < 0:
                low = 0

            # Even the maximum is negative
            if high < 0:
                return False

        # We need a possibility with exactly 0 unmatched '('
        return low == 0