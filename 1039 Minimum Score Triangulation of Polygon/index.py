from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    )
        return dp[0][n - 1]


if __name__ == "__main__":
    # Example test cases
    values_list = [
        [1, 2, 3],       # Expected 6
        [3, 7, 4, 5],    # Expected 144
        [1, 3, 1, 4, 1, 5]  # Expected 13
    ]

    solver = Solution()
    for values in values_list:
        print(f"Input: {values} -> Output: {solver.minScoreTriangulation(values)}")
