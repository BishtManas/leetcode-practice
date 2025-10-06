from typing import List

def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    i = 0
    n = len(intervals)

    # add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # add the merged/new interval
    res.append(newInterval)

    # add the rest
    while i < n:
        res.append(intervals[i])
        i += 1

    return res

if __name__ == "__main__":
    tests = [
        ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
        ([], [5,7], [[5,7]]),
        ([[1,5]], [2,3], [[1,5]]),
        ([[1,2],[3,4]], [5,6], [[1,2],[3,4],[5,6]]),
    ]

    for intervals, newInterval, expected in tests:
        result = insert_interval([iv.copy() for iv in intervals], newInterval.copy())
        print("intervals =", intervals, "new =", newInterval, "->", result, "expected =", expected)
        assert result == expected, f"Test failed: got {result}, expected {expected}"
    print("All tests passed.")
