class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(x - z) 
        b = abs(y - z) 
        if a == b :
            return 0
        elif a > b :
            return 2
        else :
            return 1
        
ans = Solution()
print('''Example 1:

Input: x = 2, y = 7, z = 4''')
print('Output:', ans.findClosest(2, 7, 4))
print()
print('''Example 2:

Input: x = 2, y = 5, z = 6''')
print('Output:', ans.findClosest(2, 5, 6))
print()
print('''Example 3:

Input: x = 1, y = 5, z = 3''')
print('Output:', ans.findClosest(1, 5, 3))
print()
print("\033[1mFor Explaination check readme file\033[0m") # This is for bold text 
print()