class Solution:
    def sortColors(self, nums):
        low = 0          # pointer for 0's
        mid = 0          # pointer for 1's (current)
        high = len(nums) - 1  # pointer for 2's

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
