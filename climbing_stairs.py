class Solution:
    def climbStairs(self, n: int) -> int:
        #dynamic programming
        #suppose u r on nth step
        #previous step couldve been n-1 or n-2
        #ways(n) = ways(n-1) + ways(n-2)
        #base cases: n=1 --> 1 way

        if n <= 2: return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1): 
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
