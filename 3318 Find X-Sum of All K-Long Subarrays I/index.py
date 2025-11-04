from collections import Counter

def findXSum(nums, k, x):
    n = len(nums)
    ans = []

    for i in range(n - k + 1):
        window = nums[i:i + k]
        count = Counter(window)
        sorted_items = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
        top_x = {num for num, _ in sorted_items[:x]}
        total = sum(num for num in window if num in top_x)
        ans.append(total)

    return ans


# ---------- Example Runs ----------
nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2
print(findXSum(nums, k, x))  # Expected output: [6, 10, 12]

nums = [3, 8, 7, 8, 7, 5]
k = 2
x = 2
print(findXSum(nums, k, x))  # Expected output: [11, 15, 15, 15, 12]
