# file: leetcode_3027.py
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        ans = 0

        for i in range(n):
            ay = points[i][1]
            curr_max = float('-inf')
            for j in range(i + 1, n):
                by = points[j][1]
                if by > ay:
                    continue
                if curr_max < by:
                    ans += 1
                if by > curr_max:
                    curr_max = by

        return ans

if __name__ == "__main__":
    # Example usage for VS Code
    sol = Solution()

    points1 = [[1,1],[2,2],[3,3]]
    print(sol.numberOfPairs(points1))  # Expected 0

    points2 = [[6,2],[4,4],[2,6]]
    print(sol.numberOfPairs(points2))  # Expected 2

    points3 = [[3,1],[1,3],[1,1]]
    print(sol.numberOfPairs(points3))  # Expected 2

    # You can add more custom tests below
    points4 = [[1010,i*1000] for i in range(1,40)]
    print(sol.numberOfPairs(points4))
