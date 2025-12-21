class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        # This array tells whether row i is already confirmed
        # to be strictly smaller than row i+1
        sorted_rows = [False] * (n - 1)
        
        deletions = 0
        
        for col in range(m):
            # Check if this column breaks lexicographic order
            bad = False
            for i in range(n - 1):
                if not sorted_rows[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break
            
            if bad:
                deletions += 1
                continue
            
            # Update sorted_rows where order is confirmed
            for i in range(n - 1):
                if not sorted_rows[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_rows[i] = True
        
        return deletions
