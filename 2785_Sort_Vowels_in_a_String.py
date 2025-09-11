def sort_vowels_by_ascii(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)

    # Step 1: Get positions of vowels and the vowels themselves
    vowel_positions = [i for i, ch in enumerate(s_list) if ch in vowels]
    vowel_chars = [s_list[i] for i in vowel_positions]

    # Step 2: Sort vowels based on ASCII values (default behavior of sorted)
    vowel_chars_sorted = sorted(vowel_chars)

    # Step 3: Put them back in original positions
    for i, ch in zip(vowel_positions, vowel_chars_sorted):
        s_list[i] = ch

    return ''.join(s_list)


print(sort_vowels_by_ascii("Leetcode"))  # Leetcdeo
print(sort_vowels_by_ascii("hEllOaU"))   # hEOlUaU
print(sort_vowels_by_ascii("AeiOU"))     # AOUei

