class Spreadsheet:
    def __init__(self, rows: int):
        """Initialize a spreadsheet with the given number of rows and 26 columns (A-Z)."""
        self.rows = rows
        self.cols = 26  # 'A' to 'Z'
        self.grid = [[0 for _ in range(self.cols)] for _ in range(rows)]

    def _parse_cell(self, cell: str) -> tuple[int, int]:
        """
        Convert a cell label like 'A1' into a (row, col) tuple using 0-based indexing.
        Example: 'A1' -> (0, 0), 'C3' -> (2, 2)
        """
        if len(cell) < 2 or not cell[0].isalpha() or not cell[1:].isdigit():
            raise ValueError(f"Invalid cell reference: {cell}")

        col = ord(cell[0].upper()) - ord('A')
        row = int(cell[1:]) - 1

        if not (0 <= col < self.cols) or not (0 <= row < self.rows):
            raise IndexError(f"Cell out of bounds: {cell}")
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        """Set a specific cell (e.g., 'B2') to the given integer value."""
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        """Reset the specified cell's value to 0."""
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def _get_value_from_token(self, token: str) -> int:
        """
        Convert a token into a value.
        Token can be:
        - a numeric value like '42'
        - a cell reference like 'A1'
        """
        token = token.strip()
        if token.isdigit():
            return int(token)
        else:
            row, col = self._parse_cell(token)
            return self.grid[row][col]

    def getValue(self, formula: str) -> int:
        """
        Evaluate a simple formula like '=5+7', '=A1+6', or '=A1+B2'.
        Only supports '+' operations between two operands.
        """
        if not formula.startswith('='):
            raise ValueError("Formula must start with '='")

        formula_body = formula[1:]
        if '+' not in formula_body:
            raise ValueError("Only '+' operations are supported.")

        left, right = formula_body.split('+', 1)
        return self._get_value_from_token(left) + self._get_value_from_token(right)

# ----------------- Test Code -----------------
if __name__ == "__main__":
    spreadsheet = Spreadsheet(3)
    print(spreadsheet.getValue("=5+7"))     # 12
    spreadsheet.setCell("A1", 10)
    print(spreadsheet.getValue("=A1+6"))    # 16
    spreadsheet.setCell("B2", 15)
    print(spreadsheet.getValue("=A1+B2"))   # 25
    spreadsheet.resetCell("A1")
    print(spreadsheet.getValue("=A1+B2"))   # 15
