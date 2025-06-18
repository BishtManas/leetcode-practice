class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n % 3 == 0 :
            n = n//3
        return n == 1
    
obj = Solution()
print(obj.isPowerOfThree(27))# true
print(obj.isPowerOfThree(9))# true
print(obj.isPowerOfThree(0))# false
print(obj.isPowerOfThree(-1))# false