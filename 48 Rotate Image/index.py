# rotate_image.py

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n matrix by 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

# Helper function to print the matrix nicely
def print_matrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)
    print()

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix 1:")
    print_matrix(matrix1)

    solution.rotate(matrix1)

    print("Rotated Matrix 1:")
    print_matrix(matrix1)

    # Example 2
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    print("Original Matrix 2:")
    print_matrix(matrix2)

    solution.rotate(matrix2)

    print("Rotated Matrix 2:")
    print_matrix(matrix2)
