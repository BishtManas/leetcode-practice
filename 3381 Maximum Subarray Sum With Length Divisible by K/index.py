class Solution:
    def maxSubarraySum(self, nums, k):
        # prefix[i] = sum of nums up to i-1
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        # For each remainder group (based on index % k),
        # we store the minimum prefix sum seen so far.
        best = {}
        ans = -10**30  # very small number

        for i, p in enumerate(prefix):
            r = i % k  # remainder group

            if r in best:
                # subarray sum = prefix[i] - smallest prefix with same mod
                ans = max(ans, p - best[r])

            # update minimum prefix value for this remainder group
            if r not in best:
                best[r] = p
            else:
                best[r] = min(best[r], p)

        return ans
