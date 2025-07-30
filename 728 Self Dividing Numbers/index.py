def is_self_dividing(num):
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            return False
    return True

def self_dividing_numbers(left, right):
    result = []
    for i in range(left, right + 1):
        if is_self_dividing(i):
            result.append(i)
    return result

if __name__ == "__main__":
    left = int(input("Enter the left value of the range: "))
    right = int(input("Enter the right value of the range: "))

    print("\nSelf-dividing numbers in this range:")
    print(self_dividing_numbers(left, right))
