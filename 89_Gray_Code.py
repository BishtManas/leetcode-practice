def gray_code(n: int) -> list[int]:
    result = [0]
    for i in range(n):
        result += [x | (1 << i) for x in reversed(result)]
    return result

# Example usage
if __name__ == "__main__":
    n = 2
    print(gray_code(n))  # Output: [0, 1, 3, 2]
