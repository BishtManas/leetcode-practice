class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both versions by '.'
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Get the maximum length between both
        n = max(len(v1), len(v2))
        
        for i in range(n):
            # If index out of range, treat as 0
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        return 0


if __name__ == "__main__":
    # Example input (you can change these values)
    version1 = input("Enter first version: ")
    version2 = input("Enter second version: ")

    solution = Solution()
    result = solution.compareVersion(version1, version2)

    print("Comparison Result:", result)
    # -1 if version1 < version2
    #  1 if version1 > version2
    #  0 if equal
