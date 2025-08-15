def summaryRanges(nums):
    result = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
        end = nums[i]
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        i += 1
    return result

# 🔹 Test Cases
print(summaryRanges([0, 1, 2, 4, 5, 7]))        # Output: ['0->2', '4->5', '7']
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))     # Output: ['0', '2->4', '6', '8->9']
print(summaryRanges([]))                       # Output: []
print(summaryRanges([1]))                      # Output: ['1']
print(summaryRanges([1, 3]))                   # Output: ['1', '3']