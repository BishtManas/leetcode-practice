class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}

        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1

        length = 0
        odd_found = False

        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        if odd_found:
            length += 1

        return length
info = Solution()
print(info.longestPalindrome("abccccdd"))# this gives the length of the palindrome : - 7
print(info.longestPalindrome("a")) # this gives also length of the palindrome : - 1