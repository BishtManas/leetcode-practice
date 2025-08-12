def repeatedSubstringPattern(s: str) -> bool:
    # Trick: s is repeated substring if it appears in (s+s)[1:-1]
    return s in (s + s)[1:-1]

# Example testing
s = "abab"  # Change this to test other cases
print("Input:", s)
print("Output:", repeatedSubstringPattern(s))