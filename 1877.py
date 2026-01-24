class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 200:
            nums.sort()
            res = 0
            for i in range(n >> 1):
                res = max(res, nums[i] + nums[-1 - i])
            return res

        maxi = 0
        for v in nums:
            if v > maxi:
                maxi = v

        freq = [0] * (maxi + 1)
        for v in nums:
            freq[v] += 1

        i, j = 0, maxi
        while i <= maxi and freq[i] == 0:
            i += 1
        while j >= 0 and freq[j] == 0:
            j -= 1

        res = 0
        k = n // 2
        while k > 0:
            res = max(res, i + j)
            freq[i] -= 1
            freq[j] -= 1

            if freq[i] == 0:
                while i <= maxi and freq[i] == 0:
                    i += 1

            if freq[j] == 0:
                while j >= 0 and freq[j] == 0:
                    j -= 1

            k -= 1

        return res
