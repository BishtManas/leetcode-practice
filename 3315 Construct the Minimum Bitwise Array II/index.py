from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            # If n is even, impossible
            if n % 2 == 0:
                ans.append(-1)
                continue

            k = 0
            # Find the largest k such that:
            # - bit k is 1
            # - all lower bits (0 to k-1) are 1
            while True:
                if (n >> k) & 1 == 0:
                    break
                k += 1

            # k-1 is the largest valid position
            k -= 1

            # Construct the minimum x
            x = ((n >> (k + 1)) << (k + 1)) | ((1 << k) - 1)
            ans.append(x)

        return ans
if __name__ == "__main__":
    sol = Solution()
    print(f'answe is : {sol.minBitwiseArray(nums = [2,3,5,7])}')