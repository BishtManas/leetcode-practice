from collections import Counter

def maxFrequencyElements(nums: list[int]) -> int:
    # Step 1: Count frequency of each number
    freq = Counter(nums)

    # Step 2: Find the maximum frequency
    max_freq = max(freq.values())

    # Step 3: Add up all occurrences of numbers having this max frequency
    result = sum(count for count in freq.values() if count == max_freq)

    return result


# ---------- For VS Code Testing ----------
if __name__ == "__main__":
    # Example input
    nums = [1, 2, 2, 3, 1, 4]
    print("Input:", nums)
    print("Output:", maxFrequencyElements(nums))  # Expected: 4
