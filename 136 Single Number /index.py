class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result
info = Solution()
print(info.singleNumber([1,1,2,2,3,4,4,5,5]))# this will return "3" because "3" appear only one times that's why this return "3".