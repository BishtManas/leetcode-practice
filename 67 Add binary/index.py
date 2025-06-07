def addBinary(a, b):
    # Convert binary strings to integers
    num1 = int(a, 2)
    num2 = int(b, 2)
    
    # Add them
    total = num1 + num2
    
    # Convert the result back to binary string (without '0b' prefix)
    return bin(total)[2:]

# Example usage:

a = "1010"
b = "1011"

result = addBinary(a, b)
print(f"Sum of {a} and {b} in binary is: {result}")
