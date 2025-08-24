def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  
    left = 0          
    max_length = 0    

    for right in range(len(s)):
        
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(f"Input: {s1} → Output: {lengthOfLongestSubstring(s1)}") 
    print(f"Input: {s2} → Output: {lengthOfLongestSubstring(s2)}")  
    print(f"Input: {s3} → Output: {lengthOfLongestSubstring(s3)}")  

   
    s = input("Enter a string: ")
    print("Longest substring length:", lengthOfLongestSubstring(s))