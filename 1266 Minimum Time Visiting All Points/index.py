from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(len(points)-1) :
            curr_p = points[i]
            next_p = points[i+1]

            dx = abs(next_p[0]-curr_p[0])
            dy = abs(next_p[1]-curr_p[1])

            total_time += max(dx,dy)
        return total_time