class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n = n // 4

        return n == 1


# Test cases
sol = Solution()
print(sol.isPowerOfFour(16))  # True
print(sol.isPowerOfFour(5))   # False
print(sol.isPowerOfFour(1))   # True
print(sol.isPowerOfFour(64))  # True
print(sol.isPowerOfFour(0))   # False