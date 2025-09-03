class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result
# Time complexity: O(log n)
print()
ans = Solution() 
print('Example 1:\nInput: x = 2.00000, n = 10')   
print(f'output : {ans.myPow(2.00000, 10)}')
print()# Output: 1024.00000
print('Example 2:\nInput: x = 2.10000, n = 3')
print(f'output : {ans.myPow(2.10000, 3)}')   # Output: 9.26100    
print()                                                            
