class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(0)  # add a new element at the end
            for j in range(i, 0, -1):  # update from back to front
                row[j] = row[j] + row[j - 1]
        return row
info = Solution()
print(info.getRow(3))
print(info.getRow(0))
print(info.getRow(1))