class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)

        # Walk through the bits
        while i < n - 1:
            if bits[i] == 1:
                i += 2   # two-bit character
            else:
                i += 1   # one-bit character

        # If we stopped exactly at last index → last char is 1-bit
        return i == n - 1
