def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        val = matrix[row][col]
        
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# ----------------------------
# Example usage in VS Code
# ----------------------------
if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    
    result = searchMatrix(matrix, target)
    print("Found?" , result)