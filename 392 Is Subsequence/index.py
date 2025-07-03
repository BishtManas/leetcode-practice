class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # i for s, j for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer in s if characters match
            j += 1  # Always move pointer in t

        return i == len(s)  # If i reached end, all chars in s matched in order
info = Solution()
print(info.isSubsequence("abc","ahbgdc"))# True
print(info.isSubsequence("axc","ahbgdc"))# False