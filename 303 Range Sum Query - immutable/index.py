class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# ✅ Example usage — you can change these values to test
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)

    print("Sum from 0 to 2:", numArray.sumRange(0, 2))  # Output: 1
    print("Sum from 2 to 5:", numArray.sumRange(2, 5))  # Output: -1
    print("Sum from 0 to 5:", numArray.sumRange(0, 5))  # Output: -3
