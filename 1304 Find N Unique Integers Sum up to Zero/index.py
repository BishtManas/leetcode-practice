def sumZero(n: int):
    res = []
    for i in range(1, n // 2 + 1):
        res.append(i)
        res.append(-i)
    if n % 2 == 1:
        res.append(0)
    return res


# Example runs
print(sumZero(5))  # Example: [-1, 1, -2, 2, 0]
print(sumZero(3))  # Example: [-1, 1, 0]
print(sumZero(1))  # [0]