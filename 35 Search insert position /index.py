def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If not found, left will be the insert position
    return left

# Example usage:

nums = [1, 3, 5, 6]
target = 5

index = searchInsert(nums, target)
print(f"Target {target} should be at index {index}")

# Try another example:

target2 = 2
index2 = searchInsert(nums, target2)
print(f"Target {target2} should be at index {index2}")
