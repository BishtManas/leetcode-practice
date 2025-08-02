def containsNearbyDuplicate(nums, k):
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map:
            if i - index_map[num] <= k:
                return True
        index_map[num] = i

    return False

# 🚀 Example test cases
print(containsNearbyDuplicate([1,2,3,1], 3))      # True
print(containsNearbyDuplicate([1,0,1,1], 1))      # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  # False