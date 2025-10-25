def totalMoney(n: int) -> int:
    total = 0
    week_start = 1
    
    while n > 0:
        days_in_week = min(7, n)
        for i in range(days_in_week):
            total += week_start + i
        week_start += 1
        n -= days_in_week
    
    return total

print(totalMoney(4))   # Output: 10
print(totalMoney(10))  # Output: 37
print(totalMoney(20))  # Output: 96