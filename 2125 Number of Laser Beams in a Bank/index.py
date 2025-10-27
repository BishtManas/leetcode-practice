def numberOfBeams(bank):
    prev = 0
    total = 0

    for row in bank:
        count = row.count('1')
        if count > 0:
            total += prev * count
            prev = count

    return total

bank = ["011001", "000000", "010100", "001000"]
print(numberOfBeams(bank))  # Output: 8
