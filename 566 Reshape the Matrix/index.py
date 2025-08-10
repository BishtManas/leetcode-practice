# 566. Reshape the Matrix
# Function to reshape the matrix
def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    
    # If reshape is not possible, return original matrix
    if m * n != r * c:
        return mat
    
    # Flatten the matrix into a single list
    flat = [num for row in mat for num in row]
    
    # Build reshaped matrix
    new_mat = []
    for i in range(r):
        new_mat.append(flat[i * c:(i + 1) * c])
    
    return new_mat


# Main program to take input and show result
if __name__ == "__main__":
    # Example 1
    mat1 = [[1, 2], [3, 4]]
    r1, c1 = 1, 4
    print("Original matrix:", mat1)
    print("Reshaped matrix:", matrix_reshape(mat1, r1, c1))
    
    print()  # Just for spacing
    
    # Example 2
    mat2 = [[1, 2], [3, 4]]
    r2, c2 = 2, 4
    print("Original matrix:", mat2)
    print("Reshaped matrix:", matrix_reshape(mat2, r2, c2))