from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == n:
                return 0

            def try_with(new_bit: int, next_can_change: bool) -> int:
                new_mask = mask | new_bit
                if new_mask.bit_count() > k:
                    return 1 + dp(i + 1, next_can_change, new_bit)
                else:
                    return dp(i + 1, next_can_change, new_mask)

            res = 0
            orig_bit = 1 << (ord(s[i]) - ord('a'))
            res = max(res, try_with(orig_bit, can_change))

            if can_change:
                for j in range(26):
                    bit_j = 1 << j
                    if bit_j == orig_bit:
                        continue
                    res = max(res, try_with(bit_j, False))

            return res

        return dp(0, True, 0) + 1


if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    k = 2
    print(sol.maxPartitionsAfterOperations(s, k))

