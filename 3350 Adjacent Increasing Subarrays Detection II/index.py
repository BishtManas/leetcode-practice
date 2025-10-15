from typing import List

class Solution:
    def maxTwoLength(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        inc_rev = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_rev[i] = inc_rev[i + 1] + 1

        max_k = 0
        for i in range(1, n):
            k = min(inc[i - 1], inc_rev[i])
            if k > max_k:
                max_k = k

        return max_k

# 🧪 Example test cases
if __name__ == "__main__":
    sol = Solution()

    nums1 = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
    print("Output for Example 1:", sol.maxTwoLength(nums1))  # Expected: 3

    nums2 = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
    print("Output for Example 2:", sol.maxTwoLength(nums2))  # Expected: 2

    nums3 = [1, 2]
    print("Output for Edge Case:", sol.maxTwoLength(nums3))  # Expected: 0
