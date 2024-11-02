class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for index in range(32): 
            bit = (n >> index) & 1
            output += bit << (31 - index)
        return output
