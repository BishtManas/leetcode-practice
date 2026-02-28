class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 1_000_000_007
        result = 0

        for i in range(1, n + 1):
            result = ((result << i.bit_length()) + i) % MOD

        return result

if __name__ == "__main__":
    sol = Solution()
    print(f"Answer is : {sol.concatenatedBinary(n = 1)}")
    print(f"Answer is : {sol.concatenatedBinary(n = 3)}")