def minCost(colors, neededTime):
    total_time = 0
    n = len(colors)
    
    for i in range(1, n):
        if colors[i] == colors[i - 1]:
            # Remove the one with smaller neededTime
            total_time += min(neededTime[i], neededTime[i - 1])
            # Keep the one with larger neededTime for next comparison
            neededTime[i] = max(neededTime[i], neededTime[i - 1])
    
    return total_time


# 🧪 Example test cases:
if __name__ == "__main__":
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    print("Output:", minCost(colors, neededTime))  # Expected: 3

    colors = "abc"
    neededTime = [1, 2, 3]
    print("Output:", minCost(colors, neededTime))  # Expected: 0

    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print("Output:", minCost(colors, neededTime))  # Expected: 2
