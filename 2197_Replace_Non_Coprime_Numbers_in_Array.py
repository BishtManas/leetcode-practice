# file: replace_non_coprimes.py
import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                x, y = stack[-2], stack[-1]
                g = math.gcd(x, y)
                if g == 1:
                    break
                lcm = (x * y) // g
                stack.pop()
                stack[-1] = lcm
        return stack

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1 = [6,4,3,2,7,6,2]
    print("Input:", nums1)
    print("Output:", sol.replaceNonCoprimes(nums1))  # Expected: [12,7,6]

    # Example 2
    nums2 = [2,2,1,1,3,3,3]
    print("Input:", nums2)
    print("Output:", sol.replaceNonCoprimes(nums2))  # Expected: [2,1,1,3]
