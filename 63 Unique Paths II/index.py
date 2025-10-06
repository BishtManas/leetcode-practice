def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # If start or end is blocked
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1  # starting point
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]


# 🔹 Example usage
if __name__ == "__main__":
    grid1 = [[0,0,0],[0,1,0],[0,0,0]]
    grid2 = [[0,1],[0,0]]
    
    print(uniquePathsWithObstacles(grid1))  # Output: 2
    print(uniquePathsWithObstacles(grid2))  # Output: 1
