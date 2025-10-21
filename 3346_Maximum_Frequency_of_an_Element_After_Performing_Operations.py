from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Edge case: empty list
        if not nums:
            return 0

        # Find min and max values in the list
        min_val = min(nums)
        max_val = max(nums)

        # Define upper bound for frequency array
        MAX = max_val + k

        # Step 1: Create a frequency array for values from 0..MAX
        freq = [0] * (MAX + 1)
        for v in nums:
            freq[v] += 1

        # Step 2: Create prefix sum array for quick range queries
        pref = [0] * (MAX + 1)
        running = 0
        for i in range(MAX + 1):
            running += freq[i]
            pref[i] = running

        # Helper function: Get sum of freq[l..r] efficiently
        def range_sum(l: int, r: int) -> int:
            if l > r:
                return 0
            if l <= 0:
                return pref[r]
            return pref[r] - pref[l - 1]

        ans = 0

        # Step 3: Consider each possible target value T
        for T in range(0, MAX + 1):
            l = max(0, T - k)
            r = min(MAX, T + k)

            # Count all elements that can be turned into T
            can_make = range_sum(l, r)
            already_T = freq[T] if 0 <= T <= MAX else 0

            # We can change at most 'numOperations' elements
            cand = min(can_make, already_T + numOperations)

            ans = max(ans, cand)

        return ans


# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4]
    k = 1
    numOperations = 2
    print("Maximum Frequency:", sol.maxFrequency(nums, k, numOperations))
