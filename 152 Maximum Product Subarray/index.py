class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for n in nums[1:]:
            # when multiplied by negative, max and min swap
            if n < 0:
                current_max, current_min = current_min, current_max

            current_max = max(n, current_max * n)
            current_min = min(n, current_min * n)

            result = max(result, current_max)

        return result
