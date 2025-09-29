from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Helper function to check if number has zero
        def has_zero(x: int) -> bool:
            return '0' in str(x)
        
        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]

# Example usage:
sol = Solution()
print(sol.getNoZeroIntegers(2))   # Output: [1, 1]
print(sol.getNoZeroIntegers(11))  # Output: [2, 9] or any valid pair
