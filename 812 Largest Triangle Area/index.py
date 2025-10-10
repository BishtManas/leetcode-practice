from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            # Shoelace formula for area of triangle
            return 0.5 * abs(
                p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])
            )
        
        max_area = 0
        n = len(points)
        
        # Try all combinations of 3 points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, area(points[i], points[j], points[k]))
        
        return max_area


if __name__ == "__main__":
    # Example 1
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    sol = Solution()
    print("Largest Triangle Area:", sol.largestTriangleArea(points))  # Output: 2.0

    # Example 2
    points = [[1,0],[0,0],[0,1]]
    print("Largest Triangle Area:", sol.largestTriangleArea(points))  # Output: 0.5
