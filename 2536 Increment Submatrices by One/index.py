def rangeAddQueries(n, queries):
    diff = [[0] * (n + 1) for _ in range(n + 1)]

    for r1, c1, r2, c2 in queries:
        diff[r1][c1] += 1
        diff[r1][c2 + 1] -= 1
        diff[r2 + 1][c1] -= 1
        diff[r2 + 1][c2 + 1] += 1

    # Row-wise prefix
    for i in range(n):
        for j in range(n):
            diff[i][j + 1] += diff[i][j]

    # Col-wise prefix
    for j in range(n):
        for i in range(n):
            diff[i + 1][j] += diff[i][j]

    result = [[diff[i][j] for j in range(n)] for i in range(n)]
    return result


# ▶ Example
n = 3
queries = [[1,1,2,2],[0,0,1,1]]

answer = rangeAddQueries(n, queries)
for row in answer:
    print(row)
