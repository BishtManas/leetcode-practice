import math

def arrange_coins_iterative(n):
    rows = 0
    while n >= rows + 1:
        rows += 1
        n -= rows
    return rows

def arrange_coins_math(n):
    return int((math.sqrt(1 + 8*n) - 1) // 2)

def arrange_coins_binary(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        curr = mid * (mid + 1) // 2
        if curr == n:
            return mid
        if curr < n:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Input from user
if __name__ == "__main__":
    n = int(input("Enter number of coins: "))
    print("Iterative Method:", arrange_coins_iterative(n))
    print("Math Method:", arrange_coins_math(n))
    print("Binary Search Method:", arrange_coins_binary(n))
