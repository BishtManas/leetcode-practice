from collections import deque
from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            q = deque(starts)
            for r, c in starts:
                visited.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return visited

        # Pacific Ocean touches top and left borders
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]

        # Atlantic Ocean touches bottom and right borders
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        pac_reach = bfs(pacific_starts)
        atl_reach = bfs(atlantic_starts)

        # Cells that can reach both oceans
        result = [[r, c] for (r, c) in pac_reach & atl_reach]
        return result


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    solution = Solution()
    output = solution.pacificAtlantic(heights)
    print("Cells that can flow to both oceans:")
    print(output)
