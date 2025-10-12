class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Precompute factorials and their modular inverses
        fact = [1] * (m + 1)
        invfact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        invfact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m - 1, -1, -1):
            invfact[i] = (invfact[i + 1] * (i + 1)) % MOD

        # Step 2: Precompute popcounts for final carry values (up to m)
        popcount_cache = {i: bin(i).count('1') for i in range(m + 1)}

        # Step 3: DP initialization
        # dp[j][carry][p]: sum of product terms for sequences using j elements,
        # resulting in a `carry` and `p` set bits.
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1  # Base case: 0 elements, 0 carry, 0 set bits

        # Step 4: Iterate through each number in nums
        for val in nums:
            new_dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]

            # Precompute (val^c / c!) terms for the current number
            terms = [0] * (m + 1)
            current_power = 1
            for c in range(m + 1):
                terms[c] = (current_power * invfact[c]) % MOD
                current_power = (current_power * val) % MOD

            # Iterate through all previous states
            for j in range(m + 1):
                for carry in range(m + 1):
                    for p in range(k + 1):
                        if dp[j][carry][p] == 0:
                            continue

                        # Decide the count 'c' for the current number's index
                        for c in range(m - j + 1):
                            val_at_bit = c + carry
                            carry_new = val_at_bit // 2
                            p_new = p + (val_at_bit % 2)

                            if p_new <= k:
                                contribution = (dp[j][carry][p] * terms[c]) % MOD
                                new_dp[j + c][carry_new][p_new] = \
                                    (new_dp[j + c][carry_new][p_new] + contribution) % MOD
            dp = new_dp

        # Step 5: Calculate the final result
        result_before_fact = 0
        for carry in range(m + 1):
            final_carry_popcount = popcount_cache[carry]
            for p in range(k + 1):
                if p + final_carry_popcount == k:
                    result_before_fact = (result_before_fact + dp[m][carry][p]) % MOD

        # The DP calculates sum(prod(nums[i]^c_i / c_i!)). Multiply by m! for the final answer.
        final_answer = (result_before_fact * fact[m]) % MOD
        return final_answer
if __name__ == "__main__":
    sol = Solution()
    
    m = int(input("Enter m: "))
    k = int(input("Enter k: "))
    nums = list(map(int, input("Enter space-separated nums: ").split()))

    result = sol.magicalSum(m, k, nums)
    print("Result:", result)