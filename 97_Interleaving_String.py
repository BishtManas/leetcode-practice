class Solution:
    """
    Standard Dynamic Programming Solution (O(len1 * len2) Space).
    dp[i][j] is True if s3[0...i+j-1] is an interleaving of s1[0...i-1] and s2[0...j-1].
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        # If the total length of s1 and s2 doesn't match s3, return False
        if len1 + len2 != len3:
            return False

        # Initialize the DP table with False. Dimensions: (len1 + 1) x (len2 + 1).
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]

        # Base case: Empty prefixes of s1 and s2 form an empty prefix of s3.
        dp[0][0] = True

        # Fill the first row (s1 prefix is empty, i=0)
        for j in range(1, len2 + 1):
            if s2[j - 1] == s3[j - 1] and dp[0][j - 1]:
                dp[0][j] = True
            else:
                break  # Optimization: subsequent cells will also be False

        # Fill the first column (s2 prefix is empty, j=0)
        for i in range(1, len1 + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0]:
                dp[i][0] = True
            else:
                break  # Optimization: subsequent cells will also be False

        # Fill the rest of the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                s3_char = s3[i + j - 1]

                # Check if s3_char can come from s1 (s1[i-1])
                from_s1 = (s1[i - 1] == s3_char) and dp[i - 1][j]

                # Check if s3_char can come from s2 (s2[j-1])
                from_s2 = (s2[j - 1] == s3_char) and dp[i][j - 1]

                # s3[i+j-1] can be formed if it comes from s1 OR s2.
                dp[i][j] = from_s1 or from_s2

        return dp[len1][len2]
if __name__ == '__main__':
  solution = Solution()
  s1 = "abc"
  s2 = "def"
  s3 = "adbcef"
  print(solution.isInterleave(s1, s2, s3))  # Output: True
