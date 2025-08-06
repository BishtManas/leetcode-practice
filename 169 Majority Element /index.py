def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# 🔢 Sample input
nums = [2, 2, 1, 1, 1, 2, 2]

# ✅ Call the function and print result
result = majorityElement(nums)
print("Majority Element:", result)