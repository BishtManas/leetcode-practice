def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    start, end = 0, 0

    for i in range(len(s)):
        len1 = expandFromCenter(s, i, i)      # Odd length
        len2 = expandFromCenter(s, i, i + 1)  # Even length
        max_len = max(len1, len2)
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expandFromCenter(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


if __name__ == "__main__":
    # Test cases
    s1 = "babad"
    s2 = "cbbd"
    s3 = "a"
    s4 = "ac"

    print(f"Input: {s1} → Output: {longestPalindrome(s1)}")  # Expected: "bab" or "aba"
    print(f"Input: {s2} → Output: {longestPalindrome(s2)}")  # Expected: "bb"
    print(f"Input: {s3} → Output: {longestPalindrome(s3)}")  # Expected: "a"
    print(f"Input: {s4} → Output: {longestPalindrome(s4)}")  # Expected: "a" or "c"

    # User input
    s = input("Enter a string: ")
    print("Longest Palindromic Substring:", longestPalindrome(s))