from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key= lambda a: (a.bit_count(), a))
    
if __name__ == "__main__":
    sol = Solution()
    print(f"Answer is : {sol.sortByBits(arr = [0,1,2,3,4,5,6,7,8])}")