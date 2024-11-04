class Solution:
    def sqSum(self, n: int) -> int:
        res = 0
        while n: 
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        slow = n 
        fast = self.sqSum(n)

        while slow != fast: 
            fast = self.sqSum(fast)
            fast = self.sqSum(fast)
            slow = self.sqSum(slow)

        return fast == 1
