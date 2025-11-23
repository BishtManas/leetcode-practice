class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        # Lists to store small numbers with remainder 1 and 2
        rem1 = []
        rem2 = []
        
        # Collect small remainders
        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)
        
        # Sort so smallest values come first
        rem1.sort()
        rem2.sort()
        
        # Case 1: Already divisible by 3
        if total % 3 == 0:
            return total
        
        # Case 2: remainder = 1
        if total % 3 == 1:
            remove1 = rem1[0] if len(rem1) >= 1 else float('inf')
            remove2 = rem2[0] + rem2[1] if len(rem2) >= 2 else float('inf')
            return total - min(remove1, remove2)
        
        # Case 3: remainder = 2
        if total % 3 == 2:
            remove1 = rem2[0] if len(rem2) >= 1 else float('inf')
            remove2 = rem1[0] + rem1[1] if len(rem1) >= 2 else float('inf')
            return total - min(remove1, remove2)
