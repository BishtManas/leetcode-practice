import bisect
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        # Sort the array to use binary search and sliding window
        nums.sort()

        # --- Case 1: Target T is one of nums[i] ---
        maxFreqCase1 = 0
        i = 0
        while i < n:
            T = nums[i]
            
            # Find count of elements already equal to T
            j = i
            while j < n and nums[j] == T:
                j += 1
            countEqual = j - i

            # Find all elements in the range [T - k, T + k]
            rangeStart = T - k
            rangeEnd = T + k

            # Find first index >= rangeStart
            left_idx = bisect.bisect_left(nums, rangeStart)
            # Find first index > rangeEnd
            right_idx = bisect.bisect_right(nums, rangeEnd)

            # Total elements in the valid range
            totalInRange = right_idx - left_idx

            # Changeable elements are those in range but not equal to T
            countChangeable = totalInRange - countEqual
            
            # The frequency for this T is the ones we already have,
            # plus the ones we can change (up to numOperations)
            currentFreq = countEqual + min(countChangeable, numOperations)
            maxFreqCase1 = max(maxFreqCase1, currentFreq)
            
            i = j  # Move to the next unique element

        # --- Case 2: Target T is NOT one of nums[i] ---
        # We are looking for the maximum number of elements that
        # can fit within a range of length 2*k.
        # This is a classic sliding window problem.
        
        left = 0
        maxWindow = 0
        
        for right in range(n):
            # While the window is too large (invalid)
            while nums[right] - nums[left] > 2 * k:
                left += 1
            
            # The window [left, right] is valid
            windowSize = right - left + 1
            maxWindow = max(maxWindow, windowSize)
            
        # The frequency is the size of the largest window,
        # capped by the number of operations we can perform.
        maxFreqCase2 = min(maxWindow, numOperations)

        # The final answer is the best of both cases
        return max(maxFreqCase1, maxFreqCase2)


# Example usage of the Solution class:
if __name__ == "__main__":
    # Sample input for testing
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 2
    numOperations = 3
    
    result = solution.maxFrequency(nums, k, numOperations)
    print(f"Maximum frequency: {result}")
