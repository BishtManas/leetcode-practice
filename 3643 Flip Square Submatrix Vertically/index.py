def flipSubmatrix(grid, x, y, k):
    # loop half (swap top with bottom)
    for i in range(k // 2):
        for j in range(k):
            # swap elements
            grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
            grid[x + k - 1 - i][y + j], grid[x + i][y + j]
    
    return grid