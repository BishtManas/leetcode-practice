class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        limitation = { ")" : "(" , "}" : "{" , "]" : "[" }
        for i in s :
            if i in limitation :
                if stack and stack[-1] == limitation[i]:
                    stack.pop()
                else :
                    return False 
            else :
                stack.append(i)
        return True if not stack else False 

obj = Solution()
print(obj.isValid("()[]{}"))