def partition(s: str) -> list[list[str]]:
    res = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return res


# ✅ Test Cases
print(partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(partition("a"))    # Output: [["a"]]
print(partition("abba")) # Output: [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
