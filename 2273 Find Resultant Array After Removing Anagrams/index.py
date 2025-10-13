def removeAnagrams(words):
    result = [words[0]]

    for i in range(1, len(words)):
        if sorted(words[i]) != sorted(words[i - 1]):
            result.append(words[i])
    
    return result


# 🧪 Example Test Cases
words1 = ["abba","baba","bbaa","cd","cd"]
words2 = ["a","b","c","d","e"]

print(removeAnagrams(words1))  # Output: ['abba', 'cd']
print(removeAnagrams(words2))  # Output: ['a', 'b', 'c', 'd', 'e']