def min_operations(nums, k):
    total = sum(nums)
    rem = total % k

    # If already divisible, no need to do anything
    if rem == 0:
        return 0

    # We need to reduce some values so that (total - x) % k == 0
    # That means: x % k == rem
    # Smallest x satisfying this is rem itself.
    return rem


# ---------------------------
# Example usage:
nums = [3, 9, 7]
k = 5
print(min_operations(nums, k))  # Output: 4

nums = [4, 1, 3]
k = 4
print(min_operations(nums, k))  # Output: 0

nums = [3, 2]
k = 6
print(min_operations(nums, k))  # Output: 5
