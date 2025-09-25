#!/usr/bin/env python3
from typing import List
import argparse
import pprint

def generate_spiral_matrix(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    val = 1
    max_val = n * n

    while val <= max_val:
        for c in range(left, right + 1):
            matrix[top][c] = val
            val += 1
        top += 1
        if val > max_val:
            break

        for r in range(top, bottom + 1):
            matrix[r][right] = val
            val += 1
        right -= 1
        if val > max_val:
            break

        for c in range(right, left - 1, -1):
            matrix[bottom][c] = val
            val += 1
        bottom -= 1
        if val > max_val:
            break

        for r in range(bottom, top - 1, -1):
            matrix[r][left] = val
            val += 1
        left += 1

    return matrix

def main():
    parser = argparse.ArgumentParser(description="Generate an n x n spiral matrix.")
    parser.add_argument('--n', type=int, help="Matrix size n (1 <= n <= 20).")
    args = parser.parse_args()

    if args.n is None:
        try:
            n = int(input("Enter n (1 <= n <= 20): ").strip())
        except Exception:
            print("Invalid input. Please provide an integer.")
            return
    else:
        n = args.n

    if n < 1 or n > 20:
        print("Constraint violation: n must be between 1 and 20.")
        return

    matrix = generate_spiral_matrix(n)
    pprint.pprint(matrix)

if __name__ == "__main__":
    main()
