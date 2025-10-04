from typing import List

def jump(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps

if __name__ == "__main__":
    # Example tests — you can edit or add more
    tests = [
        [2,3,1,1,4],   # expected 2
        [2,3,0,1,4],   # expected 2
        [0],           # expected 0
        [1,2],         # expected 1
    ]

    for arr in tests:
        print(f"nums = {arr} -> min jumps = {jump(arr)}")

    # If you want to take input from the user:
    # line = input("Enter list of ints (comma separated): ")
    # nums = list(map(int, line.strip().split(',')))
    # print(jump(nums))
