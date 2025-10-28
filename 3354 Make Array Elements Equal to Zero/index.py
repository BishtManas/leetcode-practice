def makeArrayElementsZero(nums):
    n = len(nums)

    
    def can_make_all_zero(nums, start, direction):
        nums = nums.copy()  
        curr = start
        dir = direction  

        while 0 <= curr < n:  
            if nums[curr] == 0:
                curr += dir  
            else:
                nums[curr] -= 1  
                dir *= -1        
                curr += dir      


        return all(x == 0 for x in nums)

    valid_count = 0


    for i in range(n):
        if nums[i] == 0:
            if can_make_all_zero(nums, i, -1):
                valid_count += 1
            if can_make_all_zero(nums, i, 1):
                valid_count += 1

    return valid_count


# Example 1
nums1 = [1, 0, 2, 0, 3]
print(makeArrayElementsZero(nums1))  # Output: 2

# Example 2
nums2 = [2, 3, 4, 0, 4, 1, 0]
print(makeArrayElementsZero(nums2))  # Output: 0
