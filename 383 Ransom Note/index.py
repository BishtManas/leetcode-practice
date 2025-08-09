from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)
    
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True

# Example usage
ransomNote = input("Enter ransom note: ")
magazine = input("Enter magazine: ")

result = canConstruct(ransomNote, magazine)
print(result)