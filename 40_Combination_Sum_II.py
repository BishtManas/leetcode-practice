from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print("Test Case 1 Output:", sol.combinationSum2(candidates, target))
    # Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]

    # Test Case 2
    candidates = [2,5,2,1,2]
    target = 5
    print("Test Case 2 Output:", sol.combinationSum2(candidates, target))
    # Expected: [[1,2,2],[5]]
