class Spreadsheet:

    def __init__(self, rows: int):
        # 26 columns ('A' to 'Z'), rows given
        self.rows = rows
        self.cols = 26
        # initialize all cells to 0
        self.grid = [[0] * self.cols for _ in range(rows)]

    def _parse_cell(self, cell: str) -> (int, int):
        """Convert cell like 'A1' -> (row, col) in 0-indexed format."""
        col = ord(cell[0]) - ord('A')  # 'A'->0, 'B'->1, ...
        row = int(cell[1:]) - 1        # 1-indexed -> 0-indexed
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def _get_value_from_token(self, token: str) -> int:
        """Token could be a number or a cell reference."""
        if token[0].isdigit():
            return int(token)
        else:
            row, col = self._parse_cell(token)
            return self.grid[row][col]

    def getValue(self, formula: str) -> int:
        # formula looks like "=X+Y"
        formula = formula[1:]  # remove '='
        left, right = formula.split('+')
        return self._get_value_from_token(left) + self._get_value_from_token(right)
# Example from problem statement
spreadsheet = Spreadsheet(3)
print(spreadsheet.getValue("=5+7"))     # 12
spreadsheet.setCell("A1", 10)
print(spreadsheet.getValue("=A1+6"))    # 16
spreadsheet.setCell("B2", 15)
print(spreadsheet.getValue("=A1+B2"))   # 25
spreadsheet.resetCell("A1")
print(spreadsheet.getValue("=A1+B2"))   # 15

