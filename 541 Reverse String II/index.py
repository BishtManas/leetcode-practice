class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
info = Solution()
print(info.reverseStr("abcdefg", 4))# this will return reversed character but only 4 letters because you enter 4 to rebverse the string.