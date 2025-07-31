def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]

    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result

# Test cases
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
print(findDisappearedNumbers([1,1]))              # Output: [2]
