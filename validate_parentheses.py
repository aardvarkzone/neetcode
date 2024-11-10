class Solution:
    def isValid(self, s: str) -> bool:
        #stack method
        #use a map that has closed as key, opened as value
        #if char is in map, check if previous thing on stack is the open
        #if char is in map but prev thing is not, then false
        #else append to stack 

        stack = []
        hash_map = {'}' : '{', ')' : '(', ']' : '['}

        for char in s: 
            if char in hash_map:
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else: return True
