def maximumEnergy(energy, k):
    n = len(energy)
    dp = energy[:]  # copy the list
    
    for i in range(n - k - 1, -1, -1):
        dp[i] += dp[i + k]
    
    return max(dp)


# Example test cases
energy = [5, 2, -10, -5, 1]
k = 3
print("Output:", maximumEnergy(energy, k))  # Expected: 3

energy = [-2, -3, -1]
k = 2
print("Output:", maximumEnergy(energy, k))  # Expected: -1
