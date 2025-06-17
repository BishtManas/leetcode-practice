class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n = n // factor  # keep dividing
        
        return n == 1


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [1, 6, 8, 14, 30, 0, 7, 100]
    
    for num in test_cases:
        result = sol.isUgly(num)
        print(f"Is {num} an ugly number? → {result}")
