class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
info = Solution()
print(info.countSegments("Hello, my name is John"))# output : 5 
print(info.countSegments("Hello"))# output : 1
