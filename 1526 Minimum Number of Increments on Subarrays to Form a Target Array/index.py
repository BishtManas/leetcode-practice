class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations
    
if __name__ == "__main__":
    obj = Solution()
    print()
    print("target = [1,2,3,2,1]")
    print(obj.minNumberOperations([1,2,3,2,1]))
    print()
    print("target = [3,1,1,2]")
    print(obj.minNumberOperations([3,1,5,4,2]))
    
