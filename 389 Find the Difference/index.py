class Solution:
    def findTheDifference(self, s, t):
        result = 0
        for char in s:
            result ^= ord(char)  # XOR all characters in s
        for char in t:
            result ^= ord(char)  # XOR all characters in t
        return chr(result)  # Convert back to character
info = Solution()
print(info.findTheDifference("abc","abcd"))# output "d"
