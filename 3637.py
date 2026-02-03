class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return [*islice((q for q,_ in 
            groupby((v<u)-(v>u) for v,u in pairwise(a))),4)]==[1,-1,1]
