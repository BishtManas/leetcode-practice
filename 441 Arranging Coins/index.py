import math

def arrange_coins(n):
    return int((math.sqrt(1 + 8 * n) - 1) // 2)

# LeetCode Examples
examples = [5, 8]

for n in examples:
    print(f"Input: n = {n}")
    print(f"Output: {arrange_coins(n)}\n")