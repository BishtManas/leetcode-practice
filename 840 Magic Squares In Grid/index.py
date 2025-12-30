from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # helper function to check a 3x3 magic square
        def isMagic(r, c):
            nums = set()

            # collect numbers and check range 1 to 9
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])

            # must contain exactly numbers 1 to 9
            if len(nums) != 9:
                return False

            s = sum(grid[r][c:c+3])  # sum of first row

            # check rows
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != s:
                    return False

            # check columns
            for j in range(c, c + 3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != s:
                    return False

            # check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        # scan all possible 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
