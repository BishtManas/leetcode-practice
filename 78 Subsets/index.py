from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])  # Save a copy of the current subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

# Test the function
if __name__ == "__main__":
    nums = [1, 2, 3]  # You can change this input to test other cases
    sol = Solution()
    subsets = sol.subsets(nums)
    print("Subsets of", nums, "are:")
    print(subsets)
