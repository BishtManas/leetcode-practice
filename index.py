class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try skipping left or right character
                return is_pali_range(left + 1, right) or is_pali_range(left, right - 1)
            left += 1
            right -= 1
        return True
info = Solution()
print(info.validPalindrome('aba'))# output : true
print(info.validPalindrome('abcd'))# output : false
print(info.validPalindrome('abce'))# output : false
