class Solution:
    def moveZeroes(self, nums):
        n = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
        for i in range(n, len(nums)):
            nums[i] = 0
        return nums
info = Solution()
print(info.moveZeroes([1,0,0,0,2,3,4,5,6,7,4,3]))