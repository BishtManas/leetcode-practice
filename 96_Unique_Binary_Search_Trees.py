def num_trees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    return dp[n]

# Example usage
if __name__ == "__main__":
    n = 3
    print(num_trees(n))  # Output: 5
