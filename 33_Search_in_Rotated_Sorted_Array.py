class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        return -1
    
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0 ))
print(sol.search([4,5,6,7,0,1,2], 3 ))
print(sol.search([1], 0 ))
