class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        count = 0

        for word in text.split():
            if not any(letter in broken_set for letter in word):
                count += 1

        return count
# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    print(solution.canBeTypedWords("hello world", "ad"))  # Output: 1
    
    # Test Case 2
    print(solution.canBeTypedWords("leet code", "lt"))    # Output: 1
    
    # Test Case 3
    print(solution.canBeTypedWords("leet code", "e"))     # Output: 0
