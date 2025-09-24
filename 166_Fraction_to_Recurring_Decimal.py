def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    res = []

    # Check if result is negative
    if (numerator < 0) ^ (denominator < 0):
        res.append("-")

    # Work with absolute values
    numerator, denominator = abs(numerator), abs(denominator)

    # Integer part
    res.append(str(numerator // denominator))
    remainder = numerator % denominator
    if remainder == 0:
        return "".join(res)

    res.append(".")

    # Map to store remainders and their positions
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            res.insert(remainder_map[remainder], "(")
            res.append(")")
            break

        remainder_map[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(res)


# --------------------
# Testing in VS Code
# --------------------
if __name__ == "__main__":
    print(fractionToDecimal(1, 2))     # "0.5"
    print(fractionToDecimal(2, 1))     # "2"
    print(fractionToDecimal(4, 333))   # "0.(012)"
    print(fractionToDecimal(1, 6))     # "0.1(6)"
