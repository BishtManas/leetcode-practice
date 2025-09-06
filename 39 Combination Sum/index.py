from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example test cases
    print('''Example 1:

Input: candidates = [2,3,6,7], target = 7''')
    print('Output:', sol.combinationSum([2, 3, 6, 7], 7))  # Expected [[2,2,3],[7]]
    print()
    print('''Example 2:

Input: candidates = [2,3,5], target = 8''')
    print('Output:', sol.combinationSum([2, 3, 5], 8))  # Expected [[2,2,2,2],[2,3,3],[3,5]]
    print()
    print('''Example 3:

Input: candidates = [2], target = 1''')
    print('Output:', sol.combinationSum([2], 1))  # Expected []
    print()
