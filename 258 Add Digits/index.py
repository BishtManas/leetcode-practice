class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

# Test
s = Solution()
print(s.addDigits(38))   # Output: 2
print(s.addDigits(0))    # Output: 0
print(s.addDigits(123))  # Output: 6