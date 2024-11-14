class Solution:
    def longestPalindrome(self, s: str) -> str:
        #first lets look at trivial cases
        if not s: return ""
        n = len(s)
        if n == 1: return s

        #DP problem - why? because we can split this problem up into smaller problems
        #if s[i+1, j-1] is palindrome and s[i] == s[j]: s[i, j] is valid palindrome
        #if len = 1, always valid 
        #if j = i + 1 and s[i] == s[j], true
        #iterate over the gap of each substring (j = gap + i)

        output = ""

        #1) output: longest palindrome substring
        #2) variables to track: start and end of possible palindromes
        #3) table stores bool

        dp = [[False] * n for _ in range(n)]

        for gap in range(n):
            for i in range(n-gap):
                j = gap + i
                
                if gap == 0 or\
                   gap == 1 and s[i] == s[j] or\
                   gap > 1 and s[i] == s[j] and dp[i+1][j-1]:
                   dp[i][j] = True
                
                if dp[i][j] and len(output) < j - i + 1:
                    output = s[i:j+1]

        return output
        

        
