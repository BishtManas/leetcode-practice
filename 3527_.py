class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        res = 0
        while any(starmap(gt,pairwise(a))):
            q,i = min(zip(map(sum,pairwise(a)),count()))
            res,a = res+1,a[:i]+[q]+a[i+2:]
            
        return res
