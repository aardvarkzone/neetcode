class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #convert wordDict to set for faster lookup
        wordSet = set(wordDict)
        #use memoization dict to store computed results
        memo = {}

        #recursion: 
            #check if substring s[index:] can be segmented
            #base case: end of string = true
            
        def dfs(index): 
            if index == len(s):
                return True
            
            if index in memo: 
                return memo[index]

            for word in wordSet: 
                #check if word can fit in the substring index
                #if two conditions are met: 
                    #len of word doesnt exceed remaining len of string
                    #if word == s[index  : index + len(word)] --> dfs(index + word length)
                word_len = len(word) 
                if ((index + word_len) <= len(s) and s[index : index + word_len] == word):
                    if (dfs(index + word_len)): 
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        
        return dfs(0)
