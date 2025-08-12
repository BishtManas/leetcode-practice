def findErrorNums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1

    # Find duplicate
    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    # Find missing number
    missing = (n * (n + 1)) // 2 - sum(num_set)
    return [duplicate, missing]

# Example testing
nums = [1, 2, 2, 4]  # Change this to test other cases
print("Input:", nums)
print("Output:", findErrorNums(nums))