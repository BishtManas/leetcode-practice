def hasIncreasingSubarrays(nums, k):
    n = len(nums)

    def is_increasing(start):
        for i in range(start, start + k - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True

    for i in range(n - 2 * k + 1):
        if is_increasing(i) and is_increasing(i + k):
            return True
    return False


# Example Tests
nums1 = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
k1 = 3
print(hasIncreasingSubarrays(nums1, k1))  # Output: True

nums2 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
k2 = 5
print(hasIncreasingSubarrays(nums2, k2))  # Output: False
