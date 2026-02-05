from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + x) % n] for i, x in enumerate(nums)]
    
if __name__ == "__main__":
    sol = Solution()
    print(f"Answer is : {sol.constructTransformedArray(nums = [3,-2,1,1])}")