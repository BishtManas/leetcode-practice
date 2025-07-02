class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handle negative numbers using 2's complement
        if num < 0:
            num += 2 ** 32
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num = num // 16
        
        return result
info = Solution()
print(info.toHex(26))# output :- "1a"