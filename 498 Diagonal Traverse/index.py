def findDiagonalOrder(mat):
    if not mat or not mat[0]:
        return []
    
    m, n = len(mat), len(mat[0])
    result = []
    row, col = 0, 0
    direction = 1  
    
    for _ in range(m * n):
        result.append(mat[row][col])
        
        if direction == 1:
            if col == n - 1:
                row += 1
                direction = -1
            elif row == 0:
                col += 1
                direction = -1
            else:
                row -= 1
                col += 1
        else:  
            if row == m - 1:
                col += 1
                direction = 1
            elif col == 0:
                row += 1
                direction = 1
            else:
                row += 1
                col -= 1
    
    return result


if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print("Input:", mat)
    print("Diagonal Order:", findDiagonalOrder(mat))
