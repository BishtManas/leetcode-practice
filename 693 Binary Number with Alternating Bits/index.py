class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
    
if __name__ == "__main__":
    sol = Solution()
    print(f"Answer is : {sol.hasAlternatingBits(n = 5)}")
    print(f"Answer is : {sol.hasAlternatingBits(n = 7)}")