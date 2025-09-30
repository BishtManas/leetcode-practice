def triangularSum(nums: list[int]) -> int:
    while len(nums) > 1:
        newNums = []
        for i in range(len(nums) - 1):
            newNums.append((nums[i] + nums[i+1]) % 10)
        nums = newNums
    return nums[0]

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Input:", nums)
    print("Triangular Sum:", triangularSum(nums))

    nums = [5]
    print("\nInput:", nums)
    print("Triangular Sum:", triangularSum(nums))
