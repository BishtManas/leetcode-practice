class Solution:
    def minimumOperations(self, nums):
        ops = 0
        for x in nums:
            r = x % 3
            # If remainder is 1 → either subtract 1 or add 2
            # If remainder is 2 → either subtract 2 or add 1
            # Best move is always: min(r, 3 - r)
            ops += min(r, 3 - r)
        return ops
