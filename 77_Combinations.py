from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # If we have k numbers in the current combination, add it to results
            if len(path) == k:
                res.append(path[:])
                return

            # Try all possible numbers starting from 'start' to 'n'
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # remove last added number (backtrack)

        backtrack(1, [])
        return res


if __name__ == "__main__":
    # Example 1
    n = 4
    k = 2
    solution = Solution()
    output = solution.combine(n, k)
    print("All possible combinations of", k, "numbers from 1 to", n, ":")
    print(output)
