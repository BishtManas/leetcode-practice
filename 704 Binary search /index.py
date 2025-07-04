class solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) -1
        while left<=right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return -1
info = solution()
print(info.binary_search([1,34,45,67,89,100], 100))# output : 5
print(info.binary_search([1,34,45,67,89,100], 101))# output : -1 because 101 is not present in this list.