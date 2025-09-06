import sys
import math
from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def prefix(n: int) -> int:
            if n <= 0:
                return 0
            res = 0
            base = 1  # 4^0
            steps = 1
            while base <= n:
                next_base = base * 4
                # numbers in [base, next_base-1]
                high = min(n, next_base - 1)
                count = high - base + 1
                res += count * steps
                base = next_base
                steps += 1
            return res

        ans = 0
        for l, r in queries:
            total_steps = prefix(r) - prefix(l - 1)
            ans += (total_steps + 1) // 2
        return ans


# For VS Code testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([[1, 2], [2, 4]]))  # Expected 3
    print(sol.minOperations([[2, 6]]))          # Expected 4
