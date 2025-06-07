def climbStairs(n):
    if n <= 2:
        return n
    
    a, b = 1, 2  # ways to climb 1 step and 2 steps
    
    for _ in range(3, n + 1):
        a, b = b, a + b  # shift the window forward
    
    return b

# Example usage:

print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(5))  # Output: 8
