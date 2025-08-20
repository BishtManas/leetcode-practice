def zeroFilledSubarray(nums):
    count = 0
    zeros = 0

    for num in nums:
        if num == 0:
            zeros += 1
            count += zeros
        else:
            zeros = 0

    return count

nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
nums2 = [0, 0, 0, 2, 0, 0]
nums3 = [1, 2, 3]

print("Output 1:", zeroFilledSubarray(nums1))  # Expected 6
print("Output 2:", zeroFilledSubarray(nums2))  # Expected 9
print("Output 3:", zeroFilledSubarray(nums3))  # Expected 0