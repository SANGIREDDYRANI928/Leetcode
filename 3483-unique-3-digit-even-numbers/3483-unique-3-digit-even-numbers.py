from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        unique_numbers = set()

        # Generate all 3-digit permutations
        for num in permutations(digits, 3):  
            if num[0] != 0 and num[2] % 2 == 0:  # First digit ≠ 0, last digit is even
                unique_numbers.add(int("".join(map(str, num))))  # Convert tuple to integer

        return len(unique_numbers)  # Return the count instead of print()