class Solution:
    def nextGreatestLetter(self, letters, target):
        ans = letters[0]
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = l + (r - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                ans = letters[m]
                r = m - 1
        return ans