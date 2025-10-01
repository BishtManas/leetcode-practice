# 1518. Water Bottles
# Run this in VS Code or terminal: python water_bottles.py

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empties = numBottles

        while empties >= numExchange:
            new_full = empties // numExchange
            total += new_full
            empties = new_full + (empties % numExchange)
        
        return total


# --- Test the solution locally ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    numBottles, numExchange = 9, 3
    print(f"Input: numBottles={numBottles}, numExchange={numExchange}")
    print("Output:", sol.numWaterBottles(numBottles, numExchange))  # Expected 13

    print()

    # Example 2
    numBottles, numExchange = 15, 4
    print(f"Input: numBottles={numBottles}, numExchange={numExchange}")
    print("Output:", sol.numWaterBottles(numBottles, numExchange))  # Expected 19

    print()

    # Custom input
    numBottles, numExchange = 5, 5
    print(f"Input: numBottles={numBottles}, numExchange={numExchange}")
    print("Output:", sol.numWaterBottles(numBottles, numExchange))  # Try yourself
