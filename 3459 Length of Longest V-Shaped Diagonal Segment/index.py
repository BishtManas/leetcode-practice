# File: longest_v_shape.py
from functools import lru_cache
from typing import List

class Solution:
    def longestVPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]  # ↘, ↙, ↖, ↗
        clockwise = {0:1, 1:2, 2:3, 3:0}
        
        def next_val(val: int) -> int:
            if val == 1: return 2
            if val == 2: return 0
            return 2

        @lru_cache(None)
        def dfs(i: int, j: int, d: int, used_turn: bool, expected: int) -> int:
            if not (0 <= i < n and 0 <= j < m): 
                return 0
            if grid[i][j] != expected:
                return 0

            ni, nj = i + dirs[d][0], j + dirs[d][1]
            res = 1 + dfs(ni, nj, d, used_turn, next_val(expected))
            
            if not used_turn:  # allow one clockwise turn
                td = clockwise[d]
                ti, tj = i + dirs[td][0], j + dirs[td][1]
                res = max(res, 1 + dfs(ti, tj, td, True, next_val(expected)))
            
            return res
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dfs(i,j,d,False,1))
        return ans


if __name__ == "__main__":
    grid1 = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    grid2 = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    grid3 = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
    grid4 = [[1]]
    
    sol = Solution()
    print(sol.longestVPath(grid1))  # 5
    print(sol.longestVPath(grid2))  # 4
    print(sol.longestVPath(grid3))  # 5
    print(sol.longestVPath(grid4))  # 1