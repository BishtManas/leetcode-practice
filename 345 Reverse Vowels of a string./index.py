class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert to list because strings are not editable
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                # Swap vowels
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)
info = Solution()
print(info.reverseVowels("IceCreAm"))# output : - AceCreIm
print(info.reverseVowels("leetcode")) # output: - leotcede
