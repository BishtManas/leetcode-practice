class Solution:
    def isHappy(self, n):
        seen = set()
        while n!=1 and n not in seen :
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
info = Solution()
print(info.isHappy(19))# return : - True
print(info.isHappy(23))# True 
print(info.isHappy(2))# False