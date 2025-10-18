import math
from typing import List

class Solution:
    def maximumDistinctElements(self, nums: List[int], k: int) -> int:
        """
        Calculates the maximum possible number of distinct elements after
        performing the operations, using a greedy approach.
        
        The strategy is to sort the numbers and then iterate through them,
        assigning the smallest possible new distinct value to each number
        if its range [num - k, num + k] allows for it.
        """
        
        # Sort the array to process elements in increasing order.
        # This allows the greedy choice to work.
        nums.sort()
        
        count = 0  # This will store the number of distinct elements
        
        # This variable tracks the smallest integer value that
        # has not been assigned yet.
        # We initialize it to negative infinity to ensure the first
        # element can always pick a value.
        next_available = -math.inf
        
        for num in nums:
            # For the current 'num', we want to transform it into a new
            # distinct value 'v'.
            # 'v' must satisfy two conditions:
            # 1. It must be in the allowed range: num - k <= v <= num + k
            # 2. It must be a new distinct value: v >= next_available
            
            # To maximize the number of distinct elements, we greedily
            # pick the *smallest* possible 'v' that satisfies both.
            # From (1), smallest 'v' is num - k.
            # From (2), smallest 'v' is next_available.
            # So, the smallest valid 'v' we can *try* is max(num - k, next_available).
            
            target_value = max(num - k, next_available)
            
            # Now, we check if this 'target_value' is actually achievable
            # given the upper bound from condition (1).
            # Is target_value <= num + k?
            
            if target_value <= num + k:
                # Yes. We can assign 'target_value' to 'num'.
                # This creates a new distinct element.
                count += 1
                
                # We update 'next_available' to be one larger than the
                # value we just used.
                next_available = target_value + 1
            else:
                # No. 'target_value' is > num + k.
                # This implies max(num - k, next_available) > num + k.
                # Since num - k can't be > num + k (as k >= 0),
                # this must mean 'next_available > num + k'.
                # The entire range [num - k, num + k] of this element
                # consists of values that are *smaller* than the
                # 'next_available' value we need.
                # Therefore, this 'num' cannot be transformed into a new
                # distinct value. It must become a duplicate. We do nothing.
                pass
                
        return count

if __name__ == '__main__':
    # This block runs when the script is executed directly
    solver = Solution()
    
    # Example 1
    nums1 = [1, 2, 2, 3, 3, 4]
    k1 = 2
    output1 = solver.maximumDistinctElements(nums1, k1)
    print(f"Example 1:")
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {output1}")  # Expected: 6
    print("-" * 20)
    
    # Example 2
    nums2 = [4, 4, 4, 4]
    k2 = 1
    output2 = solver.maximumDistinctElements(nums2, k2)
    print(f"Example 2:")
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {output2}")  # Expected: 3
    print("-" * 20)
    
    # Additional Test Case
    nums3 = [5, 5, 5, 6, 6, 6]
    k3 = 1
    output3 = solver.maximumDistinctElements(nums3, k3)
    print(f"Additional Test Case:")
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {output3}")  # Expected: 4
    print("-" * 20)
    
    # Test Case with k=0
    nums4 = [1, 1, 2, 3, 3]
    k4 = 0
    output4 = solver.maximumDistinctElements(nums4, k4)
    print(f"Test Case k=0:")
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {output4}")  # Expected: 3
    print("-" * 20)