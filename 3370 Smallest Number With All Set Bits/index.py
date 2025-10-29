class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1
        return x


if __name__ == "__main__":
    obj = Solution()
    print("Input: n = 5")
    print(obj.smallestNumber(5),"\n")
    # print()
    print("Input: n = 10")
    print(obj.smallestNumber(10),"\n")
    # print()
    print("Input: n = 3")
    print(obj.smallestNumber(3),"\n")