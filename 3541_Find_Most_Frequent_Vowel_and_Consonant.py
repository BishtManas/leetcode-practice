from collections import Counter

def mostFrequentVowelAndConsonant(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    freq = Counter(s)

    max_vowel = 0
    max_consonant = 0

    for ch, count in freq.items():
        if ch in vowels:
            max_vowel = max(max_vowel, count)
        else:
            max_consonant = max(max_consonant, count)

    return max_vowel + max_consonant


# ✅ Test Cases
print(mostFrequentVowelAndConsonant("successes"))  # Output: 6
print(mostFrequentVowelAndConsonant("aeiaeia"))    # Output: 3
print(mostFrequentVowelAndConsonant("abcde"))      # Output: 2
print(mostFrequentVowelAndConsonant("zzz"))        # Output: 3
print(mostFrequentVowelAndConsonant("uuuiiieeaa")) # Output: 4
