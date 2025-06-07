class Solution:
    def isPalindrome(self, x: int) -> bool:
        u=str(x)
        r=u[::-1]
        return r == u
obj = Solution()
print(obj.isPalindrome(121))  
print(obj.isPalindrome(-121)) 
print(obj.isPalindrome(10))