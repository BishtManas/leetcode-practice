def hasEqualDigits(s: str) -> bool:
    while len(s) > 2:
        new_s = ""
        for i in range(len(s) - 1):
            new_digit = (int(s[i]) + int(s[i + 1])) % 10
            new_s += str(new_digit)
        s = new_s
    return s[0] == s[1]


# --------------------------
# Test cases
# --------------------------
if __name__ == "__main__":
    s1 = "3902"
    s2 = "34789"

    print(f"Input: {s1} → Output:", hasEqualDigits(s1))  # Expected: True
    print(f"Input: {s2} → Output:", hasEqualDigits(s2))  # Expected: False
