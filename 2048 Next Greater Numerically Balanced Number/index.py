class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def is_balanced(x):
            s = str(x)
            for d in set(s):
                if int(d) != s.count(d):
                    return False
            return True

        num = n + 1
        while True:
            if is_balanced(num):
                return num
            num += 1


# ✅ Example usage:
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter a number: "))
    print("Next numerically balanced number is:", sol.nextBeautifulNumber(n))
