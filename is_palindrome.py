# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #reverse string after only keeping alph/num
#         output = ''
#         for char in s: 
#             if char.isalnum(): 
#                 output += char.lower()
#         return output == output[::-1]

        
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer solution, make everything to alp/num 
        #then just check and incr left, decr right 
        new_s = ''
        for char in s: 
            if char.isalnum(): 
                new_s += char.lower()

        left = 0 
        right = len(new_s) - 1
        while left <= right: 
            if new_s[left] == new_s[right]: 
                left += 1
                right -= 1
            else: 
                return False
        return True
