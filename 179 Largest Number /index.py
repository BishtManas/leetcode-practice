from functools import cmp_to_key

def largestNumber(nums):
    # Convert all numbers to strings
    nums = list(map(str, nums))

    # Custom compare function
    def compare(a, b):
        # Compare which combination is greater
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    # Sort using the custom comparator
    nums.sort(key=cmp_to_key(compare))

    # If the largest number is "0", return "0"
    if nums[0] == "0":
        return "0"

    # Join all parts to form the final number
    return "".join(nums)

# Example test cases
print(largestNumber([10, 2]))          # Output: "210"
print(largestNumber([3, 30, 34, 5, 9])) # Output: "9534330"
