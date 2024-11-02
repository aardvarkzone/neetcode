class Solution:
    def checkValidString(self, s: str) -> bool:
        Min = 0
        Max = 0
        for char in s:
            if char == "(":
                Min += 1
                Max += 1
            elif char == ")":
                Min -= 1
                Max -= 1
            else: 
                Min -= 1
                Max += 1
            if Max < 0: return False
            if Min < 0: Min = 0
        return Min == 0
