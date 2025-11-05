def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # start of a sequence
            current_num = num
            streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                streak += 1

            longest = max(longest, streak)

    return longest


# 🧪 Example tests
print(longestConsecutive([100, 4, 200, 1, 3, 2]))   # Output: 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))   # Output: 9
print(longestConsecutive([1,0,1,2]))               # Output: 3
