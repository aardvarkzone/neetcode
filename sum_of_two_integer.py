class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0: 
            carry = (a & b) << 1
            a = (a ^ b) & 0xFFFFFFFF
            b = carry & 0xFFFFFFFF
        
        if a <= 0x7FFFFFFF: return a
        else: return ~(a ^ 0xFFFFFFFF)
