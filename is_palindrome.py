class Solution:
    def isPalindrome(self, s: str) -> bool:
        #reverse string after only keeping alph/num
        output = ''
        for char in s: 
            if char.isalnum(): 
                output += char.lower()
        return output == output[::-1]

        
        
