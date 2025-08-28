def sort_matrix_by_diagonals(grid):
    n = len(grid)

    # Dictionary to store diagonals
    diagonals = {}

    # Collect elements of each diagonal (identified by i - j)
    for i in range(n):
        for j in range(n):
            d = i - j
            if d not in diagonals:
                diagonals[d] = []
            diagonals[d].append(grid[i][j])

    # Sort diagonals based on the rule
    for d in diagonals:
        if d >= 0:  # Bottom-left triangle and main diagonal -> non-increasing
            diagonals[d].sort(reverse=True)
        else:  # Top-right triangle -> non-decreasing
            diagonals[d].sort()

    # Fill back sorted values
    for i in range(n):
        for j in range(n):
            d = i - j
            grid[i][j] = diagonals[d].pop(0)

    return grid


# Example usage:
grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
result = sort_matrix_by_diagonals(grid)
print("Sorted Matrix:")
for row in result:
    print(row)
