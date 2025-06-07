def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    # If we don't find exact square, right will be floor(sqrt(x))
    return right

# Example usage:
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2 (because sqrt(8) ≈ 2.828, floor is 2)
