import re  # needed for regex

def isPalindrome(s):
    # Remove non-alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
    # Convert to lowercase
    m = cleaned.lower()
    # Check if it equals its reverse
    return m == m[::-1]

# Example usage:

print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome(" "))                               # True (empty string is a palindrome)
