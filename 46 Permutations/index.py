def permute(nums):
    if len(nums) == 0:
        return [[]]

    p = permute(nums[1:])   # recursive call
    r = []
    for i in p:
        for j in range(len(i) + 1):
            cp = i.copy()
            cp.insert(j, nums[0])
            r.append(cp)
    return r


# Example runs
print(permute([1, 2, 3]))
# Output: [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]

print(permute([0, 1]))
# Output: [[0, 1], [1, 0]]

print(permute([1]))
# Output: [[1]]
