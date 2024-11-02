class Solution:
    def myPow(self, x: float, n: int) -> float:
        #x^n
        if x == 0: return 0
        if n == 0: return 1

        output = 1 
        power = abs(n)

        while power: 
            if power & 1: output *= x
            x *= x
            power >>= 1
        
        if (n >= 0): 
            return output
        else: return 1/output
