def countSquares(matrix):
    rows, cols = len(matrix), len(matrix[0])
    total = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and i > 0 and j > 0:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
            total += matrix[i][j]

    return total


# ✅ Test Cases
matrix1 = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]
matrix2 = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
]

print("Output 1:", countSquares(matrix1))  # Expected 15
print("Output 2:", countSquares(matrix2))  # Expected 7