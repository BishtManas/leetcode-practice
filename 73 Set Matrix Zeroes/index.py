# 73. Set Matrix Zeroes (LeetCode)
# VS Code runnable version

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        
        # Check if first row or col has zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and cols that should be zero
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update cells based on marks
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Update first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


# ---------------------------
# Example Test
# ---------------------------

if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    print("Before:")
    for row in matrix:
        print(row)

    Solution().setZeroes(matrix)

    print("\nAfter:")
    for row in matrix:
        print(row)
