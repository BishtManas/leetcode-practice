# largest_perimeter_triangle.py

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()  # Sort ascending
        for i in range(len(nums) - 1, 1, -1):
            # Check if these 3 sides can form a triangle
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0


def main():
    # Test cases
    s = Solution()
    print(s.largestPerimeter([2, 1, 2]))      # Output: 5
    print(s.largestPerimeter([1, 2, 1, 10]))  # Output: 0
    print(s.largestPerimeter([3, 6, 2, 3]))   # Output: 8


if __name__ == "__main__":
    main()
