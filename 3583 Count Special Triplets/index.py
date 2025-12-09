def count_special_triplets(nums):
    MOD = 10**9 + 7

    left = {}
    right = {}

    # Fill right frequency map
    for x in nums:
        right[x] = right.get(x, 0) + 1

    ans = 0

    for j in range(len(nums)):
        mid = nums[j]
        double = mid * 2

        right[mid] -= 1

        left_count = left.get(double, 0)
        right_count = right.get(double, 0)

        ans = (ans + left_count * right_count) % MOD

        left[mid] = left.get(mid, 0) + 1

    return ans


# Test locally
nums = [8,4,2,8,4]
print(count_special_triplets(nums))  # Expected Output: 2
