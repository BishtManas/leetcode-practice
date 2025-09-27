from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            # If we already have 4 parts and used all digits
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start:start+length]

                # Invalid if leading zero or > 255
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    # --- Predefined examples ---
    s1 = "25525511135"
    print("Input:", s1)
    print("Valid IPs:", sol.restoreIpAddresses(s1))

    s2 = "0000"
    print("\nInput:", s2)
    print("Valid IPs:", sol.restoreIpAddresses(s2))

    s3 = "101023"
    print("\nInput:", s3)
    print("Valid IPs:", sol.restoreIpAddresses(s3))

    # --- User input ---
    print("\n--- Test Your Own Input ---")
    user_s = input("Enter a string of digits: ")
    print("Valid IPs:", sol.restoreIpAddresses(user_s))
