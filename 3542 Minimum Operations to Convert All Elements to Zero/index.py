from typing import List

def min_operations(nums: List[int]) -> int:
    n = len(nums)
    ops = 0
    i = 0

    while i < n:
        if nums[i] == 0:
            i += 1
            continue

        stack = []
        while i < n and nums[i] != 0:
            x = nums[i]
            while stack and stack[-1] > x:
                stack.pop()
                ops += 1
            if not stack or stack[-1] < x:
                stack.append(x)
            i += 1

        ops += len(stack)
    return ops

if __name__ == "__main__":
    tests = [
        ([0,2], 1),
        ([3,1,2,1], 3),
        ([1,2,1,2,1,2], 4),
        ([0,0,0], 0),
        ([2,2,2], 1),
        ([5,4,3,2,1], 5),
        ([1,3,2,3,1,4,0,2,2], None)  # example mixed - prints result
    ]

    for arr, expected in tests:
        res = min_operations(arr)
        if expected is None:
            print(f"nums = {arr} -> ops = {res}")
        else:
            print(f"nums = {arr} -> ops = {res} (expected {expected})")
