def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find the pivot
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find rightmost number greater than pivot
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums


# Example runs
print(nextPermutation([1,2,3]))  # [1,3,2]
print(nextPermutation([3,2,1]))  # [1,2,3]
print(nextPermutation([1,1,5]))  # [1,5,1]
