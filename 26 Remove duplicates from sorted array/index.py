def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0  # Pointer to place the next unique element
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1  # Number of unique elements

# Example usage:
nums = [1, 1, 2, 2, 3, 4, 4, 5]

# Call the function
unique_count = removeDuplicates(nums)

# Print the results
print("Number of unique elements:", unique_count)
print("Updated list with unique elements:", nums[:unique_count])
