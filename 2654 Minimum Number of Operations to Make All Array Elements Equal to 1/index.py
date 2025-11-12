import math

def min_operations(nums):
    n = len(nums)
    
    # Step 1: check if any 1 already exists
    ones = nums.count(1)
    if ones > 0:
        return n - ones
    
    # Step 2: find smallest subarray with gcd = 1
    min_len = float('inf')
    for i in range(n):
        curr_gcd = nums[i]
        for j in range(i + 1, n):
            curr_gcd = math.gcd(curr_gcd, nums[j])
            if curr_gcd == 1:
                min_len = min(min_len, j - i + 1)
                break
    
    # Step 3: return result
    if min_len == float('inf'):
        return -1
    
    return (min_len - 1) + (n - 1)


# Example runs
nums1 = [2, 6, 3, 4]
nums2 = [2, 10, 6, 14]

print("Output 1:", min_operations(nums1))  # Expected 4
print("Output 2:", min_operations(nums2))  # Expected -1