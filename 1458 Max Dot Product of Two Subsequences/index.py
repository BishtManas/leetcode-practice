class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # Bottom Up 
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range (m + 1)]
        for i in range (m + 1):
            dp[i][n] = float('-inf')
        for i in range (n + 1):
            dp[m][i] = float('-inf')
        for i in range (m - 1, -1, -1):
            for j in range (n - 1, -1, -1):
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1],
                               nums1[i] * nums2[j] + max(dp[i + 1][j + 1], 0)
                            )
        return dp[0][0]
            
                