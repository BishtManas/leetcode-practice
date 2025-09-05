def min_operations(num1: int, num2: int) -> int:
    for k in range(1, 61):  # no need for huge loops
        N = num1 - num2 * k
        if N < 0:
            continue
        if bin(N).count("1") <= k <= N:
            return k
    return -1

if __name__ == "__main__":
    tests = [
        (3, -2),   # -> 3
        (5, 7),    # -> -1
        (13, 0),   # -> 3
        (10, -3),  # extra test
    ]
    for a, b in tests:
        print(f"num1={a}, num2={b} -> {min_operations(a, b)}")
