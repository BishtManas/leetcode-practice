import heapq
from typing import List

class Solution:
    """
    Solves the 'Swim in Rising Water' problem using Dijkstra's algorithm.
    The 'cost' to reach a cell (r, c) is the minimum time 't' 
    such that all cells on the path from (0, 0) to (r, c) have an elevation <= t.
    """
    def swimInRisingWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        
        # Priority Queue stores tuples: (max_elevation_on_path, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        
        # Visited set
        visited = set([(0, 0)])
        
        # Directions: (dr, dc)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            # Pop the cell with the smallest required maximum elevation (minimum time 't')
            t, r, c = heapq.heappop(min_heap)
            
            # Target reached
            if r == n - 1 and c == n - 1:
                return t
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        # New required time is the max of the current path max and the new cell's elevation
                        new_t = max(t, grid[nr][nc])
                        
                        heapq.heappush(min_heap, (new_t, nr, nc))
                        visited.add((nr, nc))
                        
        return -1 # Should not happen

# Example Usage for VS Code/Local Environment
if __name__ == '__main__':
    solver = Solution()

    # Example 1
    grid1 = [[0, 2], [1, 3]]
    result1 = solver.swimInRisingWater(grid1)
    print(f"Example 1 Grid: {grid1}")
    print(f"Minimum Time (Example 1): {result1}") # Expected Output: 3

    # Example 2
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]
    ]
    result2 = solver.swimInRisingWater(grid2)
    print(f"\nExample 2 Grid (Snippet): [[0,1,...], [24,23,...], ...]")
    print(f"Minimum Time (Example 2): {result2}") # Expected Output: 16