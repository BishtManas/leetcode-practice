from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Exact match

        return closest_sum

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print("Closest sum to", target1, "is:", sol.threeSumClosest(nums1, target1))
    # Expected: 2 (-1 + 2 + 1)

    # Test case 2
    nums2 = [0, 0, 0]
    target2 = 1
    print("Closest sum to", target2, "is:", sol.threeSumClosest(nums2, target2))
    # Expected: 0

    # Test case 3
    nums3 = [1, 1, 1, 0]
    target3 = -100
    print("Closest sum to", target3, "is:", sol.threeSumClosest(nums3, target3))
    # Expected: 2 (smallest possible sum)
