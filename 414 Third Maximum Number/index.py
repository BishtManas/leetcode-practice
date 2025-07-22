class Solution:
    def thirdMax(self, nums):
        first = second = third = float('-inf')
        
        for num in nums:
            if num == first or num == second or num == third:
                continue  # Skip duplicates
            
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        return third if third != float('-inf') else first
info = Solution()
print(info.thirdMax([3,2,1]))
print(info.thirdMax([2,2,3,1]))
print(info.thirdMax([2,1]))# The third distinct maximum does not exist, so the maximum (2) is returned instead.