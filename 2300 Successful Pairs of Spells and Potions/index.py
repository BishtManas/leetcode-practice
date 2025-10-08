from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        res = []
        
        for spell in spells:
            # Minimum required potion strength for current spell
            min_potion = (success + spell - 1) // spell  # ceiling division
            idx = bisect_left(potions, min_potion)
            res.append(m - idx)
        
        return res

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example input
    spells = [10, 20, 30]
    potions = [1, 2, 3, 4, 5]
    success = 100

    # Call the function
    result = solution.successfulPairs(spells, potions, success)

    # Print the result
    print("Successful pairs:", result)
