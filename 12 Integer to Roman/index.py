class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]
        
        result = ""
        for symbol, value in roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result


# Example usage
solution = Solution()

print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"