class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        x = abs(x)

        output = int(str(x)[::-1])

        if temp < 0: 
            output *= -1

        if output < -(1 << 31) or output > (1 << 31) -1:
            return 0
        
        return output
