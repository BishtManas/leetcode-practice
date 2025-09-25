def minimumTotal(triangle):
    # Start from the second last row and move upwards
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            # Update current cell with its value + min of two possible paths below
            triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
    # The top element will hold the minimum path sum
    return triangle[0][0]


if __name__ == "__main__":
    # Example 1
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print("Triangle 1:", triangle1)
    print("Minimum Path Sum:", minimumTotal(triangle1))

    # Example 2
    triangle2 = [[-10]]
    print("\nTriangle 2:", triangle2)
    print("Minimum Path Sum:", minimumTotal(triangle2))
