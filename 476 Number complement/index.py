class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Find the number of bits in 'num'
        bit_length = num.bit_length()

        # Step 2: Create a mask with all bits set to 1 for the same length
        mask = (1 << bit_length) - 1

        # Step 3: XOR num with the mask to flip the bits
        return num ^ mask
info = Solution()
print(info.findComplement(5))# output : 2
print(info.findComplement(1))# output : 0