from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()       # to track numbers we've seen
        result = []        # to store the two duplicates

        for num in nums:
            if num in seen:     # if we already saw it, it's a duplicate
                result.append(num)
            else:
                seen.add(num)   # mark it as seen

        return result


# Example usage:
if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2, 3]
    solution = Solution()
    print(solution.getSneakyNumbers(nums))   # Output: [2, 3]
