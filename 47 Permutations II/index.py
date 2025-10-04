# file: permutations_unique.py
from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in list(counter.keys()):
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path)
                    counter[num] += 1
                    path.pop()

        backtrack([])
        return res

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    nums1 = [1,1,2]
    print("Input:", nums1)
    print("Output:", sol.permuteUnique(nums1))  # Expected [[1,1,2],[1,2,1],[2,1,1]]

    # Example 2
    nums2 = [1,2,3]
    print("Input:", nums2)
    print("Output:", sol.permuteUnique(nums2))  # Expected 6 permutations
