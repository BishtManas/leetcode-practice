from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s: str) -> str:
            res = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                res.append(str(count))
                res.append(s[i])
                i += 1
            return "".join(res)
        
        seq = "1"
        for _ in range(1, n):
            seq = rle(seq)
        return seq


# For VS Code testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))  # Expected "1"
    print(sol.countAndSay(4))  # Expected "1211"
    print(sol.countAndSay(5))  # Expected "111221"