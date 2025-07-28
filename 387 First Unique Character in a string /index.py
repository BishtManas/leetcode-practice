def first_unique_char(s: str) -> int:
    # Step 1: Count characters
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Step 2: Find first unique character
    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    # Step 3: If none found
    return -1

# ------------ Main Execution Starts Here ------------

if __name__ == "__main__":
    s = input("Enter a string: ")
    result = first_unique_char(s)
    
    if result != -1:
        print(f"The first unique character is at index {result}: '{s[result]}'")
    else:
        print("There is no unique character in the string.")
