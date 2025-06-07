def plusOne(digits):
    n = len(digits)
    
    # Walk through the list backwards
    for i in reversed(range(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    # If all were 9's, we need to add a 1 at the beginning
    return [1] + [0] * n

# Example usage:

digits = [1, 2, 3]
result = plusOne(digits)
print("Result after plus one:", result)

# Another example:
digits2 = [9, 9, 9]
result2 = plusOne(digits2)
print("Result after plus one:", result2)
