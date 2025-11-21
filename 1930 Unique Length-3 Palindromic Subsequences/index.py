def countPalindromicSubsequence(s: str) -> int:
    first = {}
    last = {}
    
    # record first and last occurrence of each letter
    for i, ch in enumerate(s):
        if ch not in first:
            first[ch] = i
        last[ch] = i
    
    result = 0
    
    # check all characters a to z
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch in first:
            l = first[ch]
            r = last[ch]
            if l < r:
                middle = set(s[l+1:r])
                result += len(middle)
    
    return result


# Example test
if __name__ == "__main__":
    print(countPalindromicSubsequence("aabca"))     # 3
    print(countPalindromicSubsequence("adc"))       # 0
    print(countPalindromicSubsequence("bbcbaba"))   # 4
