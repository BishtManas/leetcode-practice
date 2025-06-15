def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        # Step 1: Start every row with 1s
        row = [1] * (i + 1)
        print(f"\nRow {i} starting with: {row}")

        # Step 2: Fill middle values if needed
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            print(f"row[{j}] = {triangle[i-1][j-1]} + {triangle[i-1][j]} = {row[j]}")

        # Step 3: Add the row to the triangle
        triangle.append(row)
        print(f"Row {i} completed: {row}")

    return triangle


# 🧪 Try running with any value
numRows = 5
result = generate_pascals_triangle(numRows)

# 🖨 Final output
print("\n✅ Final Pascal's Triangle:")
for row in result:
    print(row)
