def house_robber(nums):
    prev2 = 0
    prev1 = 0

    for num in nums:
        new_val = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = new_val

    return prev1


# Example usage
if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    print("Maximum amount that can be robbed:", house_robber(nums))
