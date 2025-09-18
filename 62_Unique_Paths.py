from math import comb

def uniquePaths(m: int, n: int) -> int:
    # Using combinatorics formula
    return comb(m + n - 2, m - 1)

# Example usage
if __name__ == "__main__":
    m = int(input("Enter m (rows): "))
    n = int(input("Enter n (columns): "))
    print("Number of unique paths:", uniquePaths(m, n))
