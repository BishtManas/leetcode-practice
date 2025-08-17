def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Example test
n = 11
print("Input:", n)
print("Output:", hammingWeight(n))  # Expected 3