# LeetCode: Just paste this class directly
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)
        
        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        
        # Step 2: Handle sign
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Overflow check
            if num > (2**31 - 1 - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num


# -------------------------------
# VS Code / Local Testing Example
# -------------------------------
def myAtoi(s: str) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    i, n = 0, len(s)
    
    while i < n and s[i] == " ":
        i += 1
    
    sign = 1
    if i < n and (s[i] == "-" or s[i] == "+"):
        if s[i] == "-":
            sign = -1
        i += 1
    
    num = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if num > (2**31 - 1 - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        num = num * 10 + digit
        i += 1
    
    return sign * num


# Example local tests
if __name__ == "__main__":
    test_cases = ["42", "   -042", "1337c0d3", "0-1", "words and 987"]
    for t in test_cases:
        print(f"Input: {t!r}, Output: {myAtoi(t)}")
