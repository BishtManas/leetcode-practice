from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        l=len(grid)
        trail_zeros=[]
        for row in grid:
            count=0
            for ele in reversed(row):
                if ele==0:
                    count+=1
                else:
                    break
            trail_zeros.append(count)
        res=0
        for i in range(l):
            req=l-i-1
            j=i
            while j<l and trail_zeros[j]<req:
                j+=1
            if j==l:
                return -1
            while j>i:
                trail_zeros[j],trail_zeros[j-1]=trail_zeros[j-1],trail_zeros[j]
                j-=1
                res+=1
        return res 
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))