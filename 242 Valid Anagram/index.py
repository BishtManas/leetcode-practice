def isAnagram(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        print('True - The strings are anagrams.')
    else:
        print('False - The strings are not anagrams.')


# Example 1
(isAnagram("anagram", "nagaram"))
# Example 2
(isAnagram("rat", "car"))
