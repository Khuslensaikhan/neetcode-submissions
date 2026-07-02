class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0

        for _ in range(32):
            # Shift result left to make room for next bit
            result <<= 1

            # Copy the last bit of n
            result |= (n & 1)

            # Remove the last bit from n
            n >>= 1

        return result
                