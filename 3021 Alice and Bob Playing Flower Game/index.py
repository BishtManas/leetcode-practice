def flower_game(n, m):
    odd_x = (n + 1) // 2
    even_x = n // 2
    odd_y = (m + 1) // 2
    even_y = m // 2
    return odd_x * even_y + even_x * odd_y

# Auto test with LeetCode examples
examples = [(3, 2), (1, 1)]

for n, m in examples:
    result = flower_game(n, m)
    print(f"Input: n = {n}, m = {m}")
    print(f"Output: {result}\n")
