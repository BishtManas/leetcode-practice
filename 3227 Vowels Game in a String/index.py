class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        for ch in s:
            if ch in vowels:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.doesAliceWin("leetcoder"))  # Expected: True
    print(sol.doesAliceWin("bbcd"))       # Expected: False
    print(sol.doesAliceWin("bcdfg"))      # Expected: False
    print(sol.doesAliceWin("ae"))         # Expected: True
