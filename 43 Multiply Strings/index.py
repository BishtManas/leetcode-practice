class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = int(num1)
        b = int (num2)
        ans = a * b 
        return str(ans)
run = Solution()
print()
print(f'Example 1: \nnum1 = "2", num2 = "3" \n\n"2" X "3" = "{run.multiply("2", "3")}"')
print()
print(f'Example 2: \nnum1 = "123", num2 = "456" \n\n"123" X "456" = "{run.multiply("123", "456")}"')
