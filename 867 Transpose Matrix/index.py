def transpose(matrix):
    rows = len(matrix[0])
    cols = len(matrix)

    transposed = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    return transposed

# 🔍 Sample test input
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ✅ Running the function and printing result
print("Transpose of matrix1:", transpose(matrix1))
print("Transpose of matrix2:", transpose(matrix2))
