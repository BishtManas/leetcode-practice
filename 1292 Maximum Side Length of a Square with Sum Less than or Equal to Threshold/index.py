from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        n=len(mat)
        m=len(mat[0])

        pre=[[0]*(m+1) for i in range(n+1)]
        sum_mat=[[0]*(m+1) for i in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                pre[i][j]=pre[i][j-1]+mat[i-1][j-1]

        for i in range(1,n+1):
            for j in range(1,m+1):
                sum_mat[i][j]=sum_mat[i-1][j]+pre[i][j]
        
        mx=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i>mx and j>mx:
                    k=mx+1
                    curr=sum_mat[i][j]-sum_mat[i-k][j]-sum_mat[i][j-k]+sum_mat[i-k][j-k]
                    if curr<=threshold:
                        mx=k
        return mx

if __name__ == "__main__":
    sol = Solution()
    print(f" answer is {sol.maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4)}")
        