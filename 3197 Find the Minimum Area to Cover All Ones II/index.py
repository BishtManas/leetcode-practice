from functools import lru_cache
from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # 2D prefix sum for O(1) submatrix counts
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            row_acc = 0
            for j in range(m):
                row_acc += grid[i][j]
                pref[i + 1][j + 1] = pref[i][j + 1] + row_acc

        def sum_region(r1: int, r2: int, c1: int, c2: int) -> int:
            if r1 > r2 or c1 > c2:
                return 0
            return (
                pref[r2 + 1][c2 + 1]
                - pref[r1][c2 + 1]
                - pref[r2 + 1][c1]
                + pref[r1][c1]
            )

        def has_row(r: int, c1: int, c2: int) -> bool:
            return sum_region(r, r, c1, c2) > 0

        def has_col(c: int, r1: int, r2: int) -> bool:
            return sum_region(r1, r2, c, c) > 0

        def shrink(r1: int, r2: int, c1: int, c2: int):
            # Trim empty borders so subproblems stay canonical
            while r1 <= r2 and not has_row(r1, c1, c2):
                r1 += 1
            while r1 <= r2 and not has_row(r2, c1, c2):
                r2 -= 1
            while c1 <= c2 and not has_col(c1, r1, r2):
                c1 += 1
            while c1 <= c2 and not has_col(c2, r1, r2):
                c2 -= 1
            return r1, r2, c1, c2

        INF = 10 ** 9

        @lru_cache(None)
        def dp_canon(r1: int, r2: int, c1: int, c2: int, k: int) -> int:
            if k == 0:
                return INF  # cannot cover non-empty with 0 rectangles
            if k == 1:
                return (r2 - r1 + 1) * (c2 - c1 + 1)

            best = (r2 - r1 + 1) * (c2 - c1 + 1)

            # Try horizontal partitions
            for mid in range(r1, r2):
                for k_top in range(0, k + 1):
                    top = dp(r1, mid, c1, c2, k_top)
                    if top >= INF:
                        continue
                    bottom = dp(mid + 1, r2, c1, c2, k - k_top)
                    if bottom >= INF:
                        continue
                    cand = top + bottom
                    if cand < best:
                        best = cand

            # Try vertical partitions
            for mid in range(c1, c2):
                for k_left in range(0, k + 1):
                    left = dp(r1, r2, c1, mid, k_left)
                    if left >= INF:
                        continue
                    right = dp(r1, r2, mid + 1, c2, k - k_left)
                    if right >= INF:
                        continue
                    cand = left + right
                    if cand < best:
                        best = cand

            return best

        @lru_cache(None)
        def dp(r1: int, r2: int, c1: int, c2: int, k: int) -> int:
            r1, r2, c1, c2 = shrink(r1, r2, c1, c2)
            if r1 > r2 or c1 > c2:
                return 0
            if k == 0:
                return INF
            return dp_canon(r1, r2, c1, c2, k)

        return dp(0, n - 1, 0, m - 1, 3)


# ----------------------------
# Example local test runner
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1, 0, 1], [1, 1, 1]]
    grid2 = [[1, 0, 1, 0], [0, 1, 0, 1]]
    grid3 = [[1, 1], [1, 0]]

    print("Example 1:", sol.minimumSum(grid1))  # Expected 5
    print("Example 2:", sol.minimumSum(grid2))  # Expected 5
    print("Custom:", sol.minimumSum(grid3))     # Expected 3