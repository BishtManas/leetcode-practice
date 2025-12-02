from collections import defaultdict

MOD = 10**9 + 7

def numberOfTrapezoids(points):
    # Step 1: group by y
    y_groups = defaultdict(int)
    for x, y in points:
        y_groups[y] += 1

    # Step 2: count horizontal segments
    seg_counts = []
    for k in y_groups.values():
        if k >= 2:
            seg_counts.append((k * (k - 1) // 2) % MOD)

    # Step 3: combine pairs of y-levels
    result = 0
    prefix_sum = 0

    for s in seg_counts:
        result = (result + prefix_sum * s) % MOD
        prefix_sum = (prefix_sum + s) % MOD

    return result


# Example test
if __name__ == "__main__":
    points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
    print(numberOfTrapezoids(points))  # expected 3
