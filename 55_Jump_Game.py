from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # We cannot reach this index
            max_reach = max(max_reach, i + jump)
        
        return True  # Able to reach the end


# ----------------------
# Test Cases (You can modify these)
# ----------------------
if __name__ == "__main__":
    solution = Solution()

    test1 = [2, 3, 1, 1, 4]
    print("Input:", test1)
    print("Can jump?", solution.canJump(test1))  # True

    test2 = [3, 2, 1, 0, 4]
    print("\nInput:", test2)
    print("Can jump?", solution.canJump(test2))  # False

    test3 = [0]
    print("\nInput:", test3)
    print("Can jump?", solution.canJump(test3))  # True

    test4 = [2, 0, 0]
    print("\nInput:", test4)
    print("Can jump?", solution.canJump(test4))  # True
