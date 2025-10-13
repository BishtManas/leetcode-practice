from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Binary search on rotated sorted array with duplicates.
        Time: average O(log n), worst-case O(n) when many duplicates
        Space: O(1)
        """
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            # If we can't tell which side is sorted because of duplicates:
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            # If left half [l..mid] is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Else right half [mid..r] is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


# ---------------------- #
# Quick test harness for VS Code
# ---------------------- #

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,5,6,0,0,1,2], 0, True),
        ([2,5,6,0,0,1,2], 3, False),
        ([1,0,1,1,1], 0, True),
        ([1,1,3,1], 3, True),
        ([1,1,1,1,1], 2, False),
        ([3,1], 1, True),
        ([4,5,6,7,0,1,2,4,4], 0, True),
    ]

    for arr, target, expected in tests:
        res = sol.search(arr, target)
        print(f"nums={arr}, target={target} -> {res} (expected: {expected})")
