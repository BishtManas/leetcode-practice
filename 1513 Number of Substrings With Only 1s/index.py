class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        curr = 0
        
        for ch in s:
            if ch == '1':
                curr += 1
            else:
                count = (count + curr * (curr + 1) // 2) % MOD
                curr = 0
        
        # Add last block if it ends with 1
        count = (count + curr * (curr + 1) // 2) % MOD
        
        return count
