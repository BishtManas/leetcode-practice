from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist=float('inf')
        for i in range(len(nums)):
            if nums[i]==target and abs(i-start)<min_dist:min_dist=abs(i-start)
        return min_dist

if __name__ == "__main__":
    sol = Solution()
    print(f"Answer is : {sol.getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3)}")