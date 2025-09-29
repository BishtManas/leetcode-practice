from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # keep searching to the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # keep searching to the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]


# --- Test cases (will run when you execute the file) ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example test cases
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))    # Output: [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))    # Output: [-1, -1]
    print(sol.searchRange([], 0))                    # Output: [-1, -1]
    print(sol.searchRange([1], 1))                   # Output: [0, 0]
