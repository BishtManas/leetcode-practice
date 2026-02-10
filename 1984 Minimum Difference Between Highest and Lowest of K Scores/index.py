from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        return  nums.sort() or min(R-L for L, R in zip(nums, nums[k-1:]))


if __name__ =="__main__":
    sol = Solution()
    print(f"Answer is : {sol.minimumDifference(nums = [90], k = 1)}")