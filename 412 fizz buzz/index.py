class Solution:
    def fizzBuzz(self, n: int):
        info = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                info.append("FizzBuzz")
            elif i % 3 == 0 :
                info.append("Fizz")
            elif i % 5 == 0:
                info.append("Buzz")
            else:
                info.append(str(i))
        return info
inf = Solution()
print(inf.fizzBuzz(10))# output : - ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']