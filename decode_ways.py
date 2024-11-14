class Solution:
    def numDecodings(self, s: str) -> int:
        #if 0, then only valid if 1 or 2 are before it "10", "20" (2)
        #if 1 and next num not 0, valid for "1" or "11-19" (10)
        #if 2 and next num not 0, valid for "2" or "21-26" (7)
        #if 3-9, valid for "3-9" (7)

        #central problem: need to find how many ways to decode a message
        #use DP: how many ways to decode sections of s
            #if section len = 1, then 1 way (as long as not 0)
            #if section len = 
        
        if not s or int(s[0]) == 0: return 0
        n = len(s)
        if n == 1: return 1 

        dp = [0] * (n + 1) #add one to account for empty string
        dp[0] = 1 #empty string
        dp[1] = 1 #only one way to decode a single digit 

        for i in range(2, n + 1): 
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i-2]
        
        return dp[n]
        
