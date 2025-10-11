class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        # dp[i] will store the number of people who learn the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1  # On day 1, one person learns the secret

        share = 0  # This keeps track of how many people are currently sharing

        for day in range(2, n + 1):
            # If someone learned the secret delay days ago, they start sharing today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD

            # If someone learned the secret forget days ago, they forget today
            if day - forget >= 1:
                share = (share - dp[day - forget] + MOD) % MOD  # Ensure non-negative

            dp[day] = share  # These many people learn the secret today

        # Now count how many people still remember the secret at the end of day n
        # These are the people who learned it in the last (forget - 1) days
        result = sum(dp[n - forget + 1 : n + 1]) % MOD
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
