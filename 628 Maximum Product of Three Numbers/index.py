def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = maximumProduct(nums)
    print("Maximum product of three numbers is:", result)
