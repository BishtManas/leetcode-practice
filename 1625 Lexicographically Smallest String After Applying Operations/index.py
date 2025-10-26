from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s

        while q:
            curr = q.popleft()
            if curr in seen:
                continue
            seen.add(curr)

            res = min(res, curr)

            # Add 'a' to all digits at odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = "".join(arr)

            # Rotate the string by 'b' positions
            rotated = curr[-b:] + curr[:-b]

            q.append(added)
            q.append(rotated)

        return res


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "5525"
    a = 9
    b = 2
    print(solution.findLexSmallestString(s, a, b))  # Output: 2050
