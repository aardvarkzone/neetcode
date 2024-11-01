class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        matching_dict = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s: 
            if char in matching_dict: 
                if stack and stack[-1] == matching_dict[char]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)

        return True if not stack else False
