def maxRunTime(n, batteries):
    batteries.sort()
    total = sum(batteries)

    left, right = 0, total // n

    def can_run(time):
        available = 0
        for b in batteries:
            available += min(b, time)
        return available >= time * n

    while left < right:
        mid = (left + right + 1) // 2
        if can_run(mid):
            left = mid
        else:
            right = mid - 1

    return left


# ----- Local testing -----
if __name__ == "__main__":
    # Example 1
    print(maxRunTime(2, [3, 3, 3]))  # Expected: 4

    # Example 2
    print(maxRunTime(2, [1, 1, 1, 1]))  # Expected: 2
