class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Start from bottom-right and work backwards
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # Starting point
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]  # Can only come from the left
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]  # Can only come from the top
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])  # Top or left

        return grid[m - 1][n - 1]
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(sol.minPathSum([[1,2,3],[4,5,6]]))          # Output: 12
