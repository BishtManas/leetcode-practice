def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    while stack:
        next_greater[stack.pop()] = -1
    
    return [next_greater[num] for num in nums1]

# Example Test
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2))  # Output: [3, -1]