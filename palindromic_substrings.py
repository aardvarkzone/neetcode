class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        n = len(s) 
        if n == 1: return n

        #strings do not have to be unique, s is always lower case inputs

        #DP problem - why? because you can divide problem into subproblems
        #for every possible substring s[i..j]:
            #valid if i == j
            #valid if i = j-1 and s[i] == s[j]
            #valid if s[i+1...j-1] is valid and s[i] == s[j]

        #therefore, need to keep track of i, j
        #2D table, where dp[i][j] returns True if valid palindrome
        #everytime we get True, increment counter
        count = 0

        dp = [[False] * n for _ in range(n)]

        for gap in range(n): 
            for i in range(n-gap):
                j = gap + i

                if i == j or\
                   i == j - 1 and s[i] == s[j] or\
                   s[i] == s[j] and dp[i+1][j-1]:
                   dp[i][j] = True
                   count += 1
        
        return count
