from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


# Local testing
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.letterCombinations("23"))  
    # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    # Example 2
    print(sol.letterCombinations(""))  
    # Expected: []
    
    # Example 3
    print(sol.letterCombinations("2"))  
    # Expected: ["a","b","c"]
