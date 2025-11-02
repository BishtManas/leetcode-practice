class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # 1 = guard, 2 = wall, 3 = guarded cell
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3  # mark as guarded
                    nr += dr
                    nc += dc
        
        # Count unguarded cells (0 = empty & unguarded)
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1
        return unguarded

if __name__ == "__main__":
    sol = Solution()
    print(sol.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))  # Output: 7
    print(sol.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))       # Output: 4
