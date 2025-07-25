class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        index_map = {val: i for i, val in enumerate(arr)}
        dp = {}
        max_len = 0

        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev < arr[i] and prev in index_map:
                    k = index_map[prev]
                    dp[i, j] = dp.get((k, i), 2) + 1
                    max_len = max(max_len, dp[i, j])
                else:
                    dp[i, j] = 2

        return max_len if max_len >= 3 else 0
info = Solution()
print(info.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))# output :- 5 because fibonacci-like: [1,2,3,5,8].
print(info.lenLongestFibSubseq([1,3,7,11,12,14,18]))# output :- 3 fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
