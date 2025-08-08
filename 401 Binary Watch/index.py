from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        
        return result

if __name__ == "__main__":
    sol = Solution()
    turned_on = 1
    times = sol.readBinaryWatch(turned_on)
    print("Possible Times:")
    for t in times:
        print(t)