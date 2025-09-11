from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            # If the current interval overlaps with the last one in merged, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

# ----------- Test Cases (you can modify these) ------------

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[1,4],[0,4]], [[0,4]])
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = sol.merge(intervals)
        print(f"Test Case {i}:")
        print(f"Input: {intervals}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Passed: {result == expected}")
        print("-" * 40)
