from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)

        # If no 1's found, area = 0
        if max_row == -1:
            return 0

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width


# ----------------------------
# Example local test runner
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0,0,1],[0,1,0],[0,0,0]]
    grid2 = [[0,0,0],[0,0,0],[0,0,0]]
    grid3 = [[1,1],[1,0]]

    print("Example 1:", sol.minimumArea(grid1))  # Expected 4 (bounding box covering (0,2) and (1,1))
    print("Example 2:", sol.minimumArea(grid2))  # Expected 0 (no 1's)
    print("Example 3:", sol.minimumArea(grid3))  # Expected 4 (2x2 area)
