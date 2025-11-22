class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Keep shifting both numbers right until they become equal
        shift = 0
        
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift back the common prefix
        return left << shift
