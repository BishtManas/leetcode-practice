def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example test
n = 43261596
print("Input:", n)
print("Output:", reverseBits(n))