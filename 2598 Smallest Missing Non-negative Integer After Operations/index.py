from collections import Counter

def findSmallestInteger(nums, value):
    count = Counter()
    
    for num in nums:
        mod = ((num % value) + value) % value
        count[mod] += 1
    
    i = 0
    while True:
        mod = i % value
        if count[mod] > 0:
            count[mod] -= 1
        else:
            return i
        i += 1

# Sample test cases
nums1 = [1, -10, 7, 13, 6, 8]
value1 = 5
print("Output 1:", findSmallestInteger(nums1, value1))  # Expected: 4

nums2 = [1, -10, 7, 13, 6, 8]
value2 = 7
print("Output 2:", findSmallestInteger(nums2, value2))  # Expected: 2
