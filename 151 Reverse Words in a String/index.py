class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()          # splits by any number of spaces
        words.reverse()            # reverse the list
        return " ".join(words)     # join back with single spaces
