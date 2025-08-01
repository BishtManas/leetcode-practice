# Simulate the "guess" API
pick = 6  # change this to test with different picked numbers

def guess(num):
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1

# Test the solution
sol = Solution()
n = 10
print("Guessed number is:", sol.guessNumber(n))
