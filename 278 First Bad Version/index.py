def isBadVersion(version):
    return version >= bad  # 'bad' is the first bad version

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example test
n = 5
bad = 4
print(firstBadVersion(n))  # Output: 4
