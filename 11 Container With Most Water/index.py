def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Calculate width and height
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_water = max(max_water, area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Maximum water that can be stored:", max_area(height))
