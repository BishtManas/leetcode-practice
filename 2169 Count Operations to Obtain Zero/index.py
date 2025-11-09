class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0

        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1

        return operations


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countOperations(10, 5))   # Output: 2
    print(sol.countOperations(2, 3))    # Output: 3