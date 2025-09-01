def solveSudoku(board):
    # Precompute sets for rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty_cells = []

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                empty_cells.append((r, c))
            else:
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)

    def backtrack(index):
        if index == len(empty_cells):
            return True  # All cells filled successfully

        r, c = empty_cells[index]
        b = (r // 3) * 3 + c // 3  # Box index

        for num in '123456789':
            if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                # Place number
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack(index + 1):
                    return True

                # Backtrack
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

        return False

    backtrack(0)


# Sample input board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print("Input Board:")
for row in board:
    print(row)

solveSudoku(board)

print("\nSolved Board:")
for row in board:
    print(row)
