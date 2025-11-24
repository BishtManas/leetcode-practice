def prefixesDivBy5(nums):
    ans = []
    current = 0

    for bit in nums:
        current = (current * 2 + bit) % 5
        ans.append(current == 0)

    return ans


# Example Run
nums = [0, 1, 1]
print(prefixesDivBy5(nums))