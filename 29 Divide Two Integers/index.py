def divide(dividend: int, divisor: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Handle overflow case
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine sign
    negative = (dividend < 0) ^ (divisor < 0)

    # Convert to positive
    dividend, divisor = abs(dividend), abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple

    # Apply sign
    if negative:
        quotient = -quotient

    # Clamp result
    return max(min(quotient, INT_MAX), INT_MIN)


if __name__ == "__main__":
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    print("Result:", divide(dividend, divisor))
