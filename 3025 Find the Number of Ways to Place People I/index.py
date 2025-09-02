from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]

                # Check if A(i) is on the upper-left side of B(j)
                if x1 <= x2 and y1 >= y2 and (x1 < x2 or y1 > y2):
                    # Check if any other point lies inside/on rectangle
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                            valid = False
                            break
                    if valid:
                        count += 1

        return count


# Example usage (VS Code / local test)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))  # 0
    print(sol.numberOfPairs([[6,2],[4,4],[2,6]]))  # 2
    print(sol.numberOfPairs([[3,1],[1,3],[1,1]]))  # 2
